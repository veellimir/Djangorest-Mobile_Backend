from typing import List, Dict

from rest_framework import generics
from rest_framework.serializers import BaseSerializer

from .serializers import (
    TaskSerializer,
    TaskStatusesSerializers,
    TasksOrganizationSerializer
)
from .models import Tasks


class TaskCreateView(generics.CreateAPIView):
    serializer_class: type[BaseSerializer] = TaskSerializer

    def perform_create(self, serializer):
        organization = serializer.validated_data['organization']
        user = self.request.user

        if not organization.members.filter(id=user.id).exists():
            raise PermissionError(
                "Данной организации не существует"
            )
        serializer.save(user=user)


class TasksOrganizationView(generics.ListAPIView):
    serializer_class: type[BaseSerializer] = TasksOrganizationSerializer

    def get_queryset(self):
        pass


class TasksStatusesListView(generics.ListAPIView):
    serializer_class: type[BaseSerializer] = TaskStatusesSerializers

    def get_queryset(self) -> List[Dict[str, str]]:
        return [{"status_task": status} for status in Tasks.STATUSES_TASKS]