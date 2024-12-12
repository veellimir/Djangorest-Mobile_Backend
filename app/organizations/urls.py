from django.urls import path
from . import views

urlpatterns = [
    path('api/organizations/create/', views.OrganizationCreateView.as_view(), name='organizations-create'),
    path('api/organizations/list/', views.OrganizationListView.as_view(), name='get_list_organizations'),
]
