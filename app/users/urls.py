from typing import List

from django.urls import path

from . import views

urlpatterns: List[path] = [
    path('api/user/me/', views.CurrentUserView.as_view(), name='current_user'),
    path('api/user/organization/', views.CurrentOrganizationUsers.as_view(), ),
]
