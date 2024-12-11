from typing import List
from django.urls import path

from . import views


urlpatterns: List[path] = [
    path("api/tasks/", views.TasksListView.as_view(), )
]