from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings

from rest_framework import serializers
from django.contrib.auth.tokens import default_token_generator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
        )


class UserPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            "old_password",
            "new_password",
            "confirm_password",
        )


class PasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, label="Email для сброса пароля")

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Пользователь с этим email не найден.")
        return value



class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, min_length=6)
    confirm_password = serializers.CharField(write_only=True, min_length=6)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Пароли не совпадают.")
        return data
