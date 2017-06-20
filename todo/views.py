from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import Template, Context
from django.views import generic
import datetime

from .models import TodoItem
# Create your views here.


def todo(request):
    return render(request, 'todo/index.html')

class TodoView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_items'

    def get_queryset(self):
        return TodoItem.objects.all()

def add_item(request):
    description = request.POST['description']
    item = TodoItem(description=description)
    item.save()
    return HttpResponseRedirect('/todo')