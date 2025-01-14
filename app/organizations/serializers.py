from rest_framework import serializers

from .models import Organization, OrganizationInvite


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


class OrganizationInviteSerializer(serializers.Serializer):
    email = serializers.CharField(
        required=True,
        help_text="Email of the registered user who will be added to the organization"
    )
    organization_id = serializers.IntegerField(
        required=True,
        help_text="ID организации"
    )

    class Meta:
        model = OrganizationInvite
        fields = [
            'organization',
            'invite',
            'invite_status'
        ]


class OrganizationCurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'created_at'
        ]


class OrganizationUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'members'
        ]
