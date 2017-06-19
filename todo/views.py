from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import datetime

# Create your views here.


def todo(request):
    return render(request, 'todo/index.html')


def hello(request):
    return HttpResponse("Todo application")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
