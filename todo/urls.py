from django.conf.urls import url
from django.conf.urls import include
from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.TodoView.as_view(), name='index'),
    url(r'add_item/$', views.TodoCreateView.as_view(), name='add_item'),
    url(r'(?P<pk>[0-9]+)/detail/$', views.TodoDetailView.as_view(), name='detail'),
    url(r'(?P<pk>[0-9]+)/delete/$', views.TodoDeleteView.as_view(), name='delete'),
    url(r'(?P<pk>[0-9]+)/update/$', views.TodoUpdateView.as_view(), name='update'),
]
