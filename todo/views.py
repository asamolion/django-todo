from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import Template, Context
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

from .models import TodoItem
from .forms import TodoItemModelUpdateForm
from .forms import TodoItemModelCreateForm
# Create your views here.


class TodoView(LoginRequiredMixin, generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_items'

    def get_queryset(self):
        return TodoItem.objects.filter(user__exact=self.request.user).filter(
            status__in=['pending', 'inprogress']).order_by('status')


class TodoCreateView(generic.CreateView):
    model = TodoItem
    # template_name = 'todo/add_item.html'
    success_url = '/todo/'
    fields = ['description', 'user']
    

class TodoDetailView(generic.DetailView):
    model = TodoItem
    template_name = 'todo/detail.html'
    context_object_name = 'item'


class TodoDeleteView(generic.DeleteView):
    model = TodoItem
    template_name = 'todo/delete.html'
    success_url = '/todo'


class TodoUpdateView(generic.UpdateView):
    model = TodoItem
    form_class = TodoItemModelUpdateForm
    template_name = 'todo/update.html'
    success_url = '/todo'
