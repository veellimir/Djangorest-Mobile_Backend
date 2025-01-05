from typing import List, Dict

from rest_framework import generics
from rest_framework.serializers import BaseSerializer
from rest_framework.exceptions import NotFound

from .serializers import (
    TaskSerializer,
    TaskStatusesSerializers,
    TasksOrganizationSerializer,
    TaskUpdateSerializers
)
from .models import Tasks
from utils.exceptions import EXCEPTION_ORGANIZATION_NOT_FOUND


class TaskCreateView(generics.CreateAPIView):
    serializer_class: type[BaseSerializer] = TaskSerializer

    def perform_create(self, serializer):
        organization = serializer.validated_data['organization']
        user = self.request.user

        if not organization.members.filter(id=user.id).exists():
            return EXCEPTION_ORGANIZATION_NOT_FOUND
        serializer.save(user=user)


class TasksOrganizationView(generics.ListAPIView):
    serializer_class: type[BaseSerializer] = TasksOrganizationSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Tasks.objects.none()
        return Tasks.objects.filter(organization__members=user)


class TaskUpdateView(generics.UpdateAPIView):
    serializer_class: type[BaseSerializer] = TaskUpdateSerializers

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise NotFound("User not authenticated.")
        return Tasks.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        task = serializer.instance
        if task.user != self.request.user:
            raise NotFound("Task not found or not editable by this user")
        serializer.save()


class TaskDeleteView(generics.DestroyAPIView):
    serializer_class: type[BaseSerializer] = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Tasks.objects.filter(user=user)


class TasksStatusesListView(generics.ListAPIView):
    serializer_class: type[BaseSerializer] = TaskStatusesSerializers

    def get_queryset(self) -> List[Dict[str, str]]:
        return [{"status_task": status} for status in Tasks.STATUSES_TASKS]
