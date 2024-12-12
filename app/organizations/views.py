from rest_framework import generics, permissions
from rest_framework.serializers import BaseSerializer

from .serializers import (
    OrganizationSerializer,
    OrganizationCurrentUserSerializer
)

from .models import Organization


class OrganizationCreateView(generics.CreateAPIView):
    permission_classes: list = [permissions.IsAuthenticated]
    serializer_class: type[BaseSerializer] = OrganizationSerializer

    def perform_create(self, serializer: BaseSerializer) -> None:
        serializer.save(owner=self.request.user)


class OrganizationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrganizationCurrentUserSerializer

    def get_queryset(self):
        return Organization.objects.filter(members=self.request.user)
