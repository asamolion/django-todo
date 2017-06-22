from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import Template, Context
from django.views import generic
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

import datetime

from .models import TodoItem
from .forms import TodoItemModelUpdateForm
from .forms import TodoItemModelCreateForm
# Create your views here.


class TodoView(LoginRequiredMixin, generic.ListView):
    """
    Main page after login, lists all the TodoItems for 
    the logged in user 
    """
    template_name = 'todo/index.html'
    context_object_name = 'todo_items'

    def get_queryset(self):
        if (self.request.user.has_perm('todo.is_manager')):
            return TodoItem.objects.order_by('status')
        else:
            return TodoItem.objects.filter(user=self.request.user).filter(
                status__in=['pending', 'inprogress']).order_by('status')


class TodoCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Generic view to create a single TodoItem for 
    the logged in user
    """
    model = TodoItem
    success_url = '/todo/'
    fields = ['description', 'user']


class TodoDetailView(LoginRequiredMixin, generic.DetailView):
    """
    displays the detail of a single item in todo list for
    a specific user
    """
    model = TodoItem
    # permission_required = 'todo.can_todo'
    template_name = 'todo/detail.html'
    context_object_name = 'item'

    def dispatch(self, request, *args, **kwargs):
        """
        Override dispatch method to handle user and manager
        permissions
        """
        item = TodoItem.objects.filter(pk=kwargs['pk']).all()[0]
        if request.user.is_authenticated:
            if request.user.has_perm('todo.is_manager'):
                return super().dispatch(request)
            if item.user.id != request.user.id:
                return redirect('todo:index')
            else:
                return super().dispatch(request)
        return super().dispatch(request)


class TodoDeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    View to delete TodoItem for specific user
    """
    model = TodoItem
    # permission_required = 'todo.can_todo'
    template_name = 'todo/delete.html'
    success_url = '/todo'

    def dispatch(self, request, *args, **kwargs):
        """
        Override dispath method to include manager permissions and
        and user access permissions
        """
        item = TodoItem.objects.filter(pk=kwargs['pk']).all()[0]
        if request.user.is_authenticated:
            if request.user.has_perm('todo.is_manager'):
                return super().dispatch(request)
            if item.user.id != request.user.id:
                return redirect('todo:index')
            else:
                return super().dispatch(request)
        return super().dispatch(request)


class TodoUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    View that updates the TodoItem for a specific user
    """
    model = TodoItem
    # permission_required = 'todo.can_todo'
    form_class = TodoItemModelUpdateForm
    template_name = 'todo/update.html'
    success_url = '/todo/'

    def get(self, request, pk):
        """
        Override get method to handle manager and
        user permissions
        """
        item = TodoItem.objects.filter(pk=pk).all()[0]
        form = TodoItemModelUpdateForm({
            'description': item.description,
            'status': item.status
        })
        if request.user.is_authenticated:
            if request.user.has_perm('todo.is_manager'):
                return render(request, 'todo/update.html', {'form': form})
            if item.user.id == request.user.id:
                return render(request, 'todo/update.html', {'form': form})
            else:
                return redirect('todo:index')
        return redirect('todo:index')
