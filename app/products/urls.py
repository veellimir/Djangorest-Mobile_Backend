from typing import List

from django.urls import path

from . import views

urlpatterns: List[path] = [
    path('api/card/', views.CardListView.as_view(), name='current_user'),
]
