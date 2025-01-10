from typing import List

from django.urls import path

from . import views

urlpatterns: List[path] = [
    path('api/user/me/', views.CurrentUserView.as_view(), ),
    path('api/user/organization/', views.CurrentOrganizationUsers.as_view(), ),
    path('api/user/me/change-password/', views.ChangePasswordView.as_view(), ),
    path('api/user/me/edit/', views.UpdateCurrentUserView.as_view(), ),
]
