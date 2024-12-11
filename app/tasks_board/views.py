from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response

from .models import Tasks
from .serializers import TasksSerializer


class TasksListView(generics.ListAPIView):
    serializer_class = TasksSerializer
    permission_classes = [AllowAny]

    def get_queryset(self) -> Response:
        return Tasks.objects.all()
