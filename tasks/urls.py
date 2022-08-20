from django.urls import re_path
from tasks import views

urlpatterns = [
    re_path(r'^$', views.get_tasks),
    re_path(r'^(?P<pk>[0-9]+)$', views.get_task),
]
