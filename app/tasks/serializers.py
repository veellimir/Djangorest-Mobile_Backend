from typing import Any
from rest_framework import serializers

from .models import Tasks, Organization


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model: type[Tasks] = Tasks
        fields: list[str] = [
            'id',
            'organization',
            'user',
            'status_task',
            'title',
            'description',
            'created_at'
        ]
        read_only_fields: list[str] = [
            'created_at'
        ]

    def validate_organization(self, organization: type[Organization]) -> Organization:
        request = self.context['request']

        if not organization.members.filter(id=request.user.id).exists():
            raise serializers.ValidationError(
                "This organization does not exist"
            )
        return organization

    def save(self, **kwargs: Any) -> Tasks:
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)


class TasksOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id',
            'user',
            'status_task',
            'title',
            'description',
            'created_at',
        ]


class TaskUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id',
            'organization',
            'user',
            'status_task',
            'title',
            'description',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'organization', 'user']



class TaskStatusesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['status_task']
        