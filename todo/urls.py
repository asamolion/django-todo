from django.conf.urls import url

from .views import hello, current_datetime, todo

app_name = 'todo'
urlpatterns = [
    url(r'^$', todo),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
]
