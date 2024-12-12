from django.urls import path
from . import views

urlpatterns = [
    path('api/tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
]
