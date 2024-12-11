from django.urls import path
from .views import OrganizationCreateView, TaskCreateView

urlpatterns = [
    path('api/organizations/create/', OrganizationCreateView.as_view(), name='organization-create'),
    path('api/tasks/create/', TaskCreateView.as_view(), name='task-create'),
]
