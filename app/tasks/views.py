from rest_framework import generics, permissions
from rest_framework.serializers import BaseSerializer

from .serializers import TaskSerializer


class TaskCreateView(generics.CreateAPIView):
    permission_classes: list = [permissions.IsAuthenticated]
    serializer_class: type[BaseSerializer] = TaskSerializer
