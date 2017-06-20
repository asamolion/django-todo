from django.conf.urls import url

from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.TodoView.as_view(), name='index'),
    url(r'add_item/$', views.add_item),
]
