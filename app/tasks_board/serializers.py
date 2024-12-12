from typing import Any

from rest_framework import serializers
from .models import Organization, Tasks


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model: type[Organization] = Organization
        fields: list[str] = [
            'id',
            'name',
            'owner',
            'members',
            'created_at'
        ]
        read_only_fields: list[str] = [
            'owner',
            'members',
            'created_at'
        ]


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
                "Вы не являетесь участником этой организации"
            )
        return organization

    def save(self, **kwargs: Any) -> Tasks:
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)


class OrganizationCurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'created_at'
        ]
