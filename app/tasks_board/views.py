from rest_framework import generics, permissions
from rest_framework.serializers import BaseSerializer

from .serializers import OrganizationSerializer, TaskSerializer


class OrganizationCreateView(generics.CreateAPIView):
    permission_classes: list = [permissions.IsAuthenticated]
    serializer_class: type[BaseSerializer] = OrganizationSerializer

    def perform_create(self, serializer: BaseSerializer) -> None:
        serializer.save(owner=self.request.user)


class TaskCreateView(generics.CreateAPIView):
    permission_classes: list = [permissions.IsAuthenticated]
    serializer_class: type[BaseSerializer] = TaskSerializer
