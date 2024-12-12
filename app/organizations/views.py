from rest_framework import generics
from rest_framework.serializers import BaseSerializer

from .serializers import (
    OrganizationSerializer,
    OrganizationCurrentUserSerializer
)

from .models import Organization


class OrganizationCreateView(generics.CreateAPIView):
    serializer_class: type[BaseSerializer] = OrganizationSerializer

    def perform_create(self, serializer: BaseSerializer) -> None:
        serializer.save(owner=self.request.user)


class OrganizationListView(generics.ListAPIView):
    serializer_class: type[BaseSerializer] = OrganizationCurrentUserSerializer

    def get_queryset(self):
        return Organization.objects.filter(members=self.request.user)
