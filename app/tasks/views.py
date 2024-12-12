from typing import List, Dict

from rest_framework import generics, permissions
from rest_framework.serializers import BaseSerializer

from .serializers import TaskSerializer, TaskStatusesSerializers
from .models import Tasks


class TaskCreateView(generics.CreateAPIView):
    serializer_class: type[BaseSerializer] = TaskSerializer


class TasksStatusesListView(generics.ListAPIView):
    serializer_class: type[BaseSerializer] = TaskStatusesSerializers

    def get_queryset(self) -> List[Dict[str, str]]:
        return [{"status_task": status} for status in Tasks.STATUSES_TASKS]