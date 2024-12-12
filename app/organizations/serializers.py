from rest_framework import serializers

from .models import Organization


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


class OrganizationCurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'created_at'
        ]
