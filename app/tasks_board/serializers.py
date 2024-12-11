from rest_framework import serializers

from .models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            "id",
            "user",
            "status_task",
            "title",
            "description",
            "created_at",
        )