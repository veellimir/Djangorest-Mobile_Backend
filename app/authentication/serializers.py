from typing import Dict

from rest_framework import serializers
from django.contrib.auth.models import User

from .utils import *


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=20,
        required=True,
        validators=[validate_username],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    email = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_email],
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
        )
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data: Dict[str, str]) -> User:
        user = User.objects.create_user(**validated_data)
        return user