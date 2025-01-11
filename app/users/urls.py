from typing import List

from django.urls import path

from . import views

urlpatterns: List[path] = [
    path('api/user/me/', views.CurrentUserView.as_view(), ),
    path('api/user/organization/', views.CurrentOrganizationUsers.as_view(), ),
    path('api/user/me/change-password/', views.ChangePasswordView.as_view(), ),
    path('api/user/me/edit/', views.UpdateCurrentUserView.as_view(), ),
    path('api/user/me/delete/', views.UserDeleteAPIView.as_view(), ),

    path('api/user/password-reset/', views.PasswordResetRequestAPIView.as_view(), name='password_reset_request'),
    path('api/user/password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),
    path('final_password/', views.final_password, name='final_password'),
]
