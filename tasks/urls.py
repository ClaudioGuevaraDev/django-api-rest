from django.urls import re_path
from tasks import views

urlpatterns = [
    re_path(r'^api/tasks$', views.handler_tasks),
    re_path(r'^api/tasks/(?P<pk>[0-9]+)$', views.handler_tasks_with_pk),
]
