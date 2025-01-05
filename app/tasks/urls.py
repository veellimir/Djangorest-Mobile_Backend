from typing import List

from django.urls import path
from . import views

urlpatterns: List[path] = [
    path('api/tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('api/tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('api/tasks/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task-edit'),
    path('api/tasks/list/', views.TasksOrganizationView.as_view(), name='task-list'),
    path('api/tasks/status/', views.TasksStatusesListView.as_view(), ),
]
