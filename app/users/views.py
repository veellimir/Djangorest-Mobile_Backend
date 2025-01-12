from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.conf import settings

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema

from app.organizations.serializers import OrganizationUsersSerializer
from app.organizations.models import Organization
from settings.env_config import CONFIG__PROJECT_DOMAIN_NAME

from .serializers import (
    UserSerializer,
    UserPasswordSerializer,
    PasswordResetEmailSerializer,
    PasswordResetConfirmSerializer
)

from utils.exceptions import (
    EXCEPTION_UNAUTHORIZED,
    EXCEPTION_USER_EMAIL,
    EXCEPTION_USER_NOT_FOUND,
    EXCEPTION_USER_PASSWORD
)


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self) -> Response:
        return self.request.user


class CurrentOrganizationUsers(generics.RetrieveAPIView):
    serializer_class = OrganizationUsersSerializer

    def get_object(self) -> Response:
        try:
            organization = Organization.objects.get(members=self.request.user)
        except Organization.DoesNotExist:
            raise NotFound("The organization has not been found or you are not a member of it.")
        return organization


class UpdateCurrentUserView(generics.UpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = UserPasswordSerializer

    def update(self, request, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            return None

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']

        if not user.check_password(old_password):
            return EXCEPTION_USER_PASSWORD

        user.set_password(new_password)
        user.save()

        return Response(
            {"message": "The password has been successfully changed."},
            status=status.HTTP_200_OK
        )


class UserDeleteAPIView(APIView):
    def delete(self, request):
        user = request.user
        if user.is_authenticated:
            user.delete()
            return Response(
                {"message": "The user has been deleted"},
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return EXCEPTION_UNAUTHORIZED


class PasswordResetRequestAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=PasswordResetEmailSerializer)
    def post(self, request):
        serializer = PasswordResetEmailSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return EXCEPTION_USER_EMAIL

            self.send_reset_email(user)

            return Response(
                {"message": "An email with instructions for password reset has been sent."},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_reset_email(self, user):
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(str(user.pk).encode())

        # TODO: изменить на CONFIG__PROJECT_DOMAIN_NAME
        # reset_url = f"http://127.0.0.1:8000/api/user/password-reset-confirm/{uid}/{token}/"
        reset_url = f"{CONFIG__PROJECT_DOMAIN_NAME}/api/user/password-reset-confirm/{uid}/{token}/"

        subject = "Восстановление пароля"
        message = render_to_string(
            'password_reset_email.html',
            {'reset_url': reset_url, 'user': user}
        )
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], html_message=message)


class PasswordResetConfirmAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return EXCEPTION_USER_NOT_FOUND

        if not default_token_generator.check_token(user, token):
            return EXCEPTION_USER_NOT_FOUND

        return render(request, 'password_reset_confirm.html', {
            'uidb64': uidb64,
            'token': token
        })

    def post(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return EXCEPTION_USER_NOT_FOUND

        if not default_token_generator.check_token(user, token):
            return EXCEPTION_USER_NOT_FOUND

        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response(
                {"message": "The password has been successfully changed."},
                status=200
            )
        return Response(serializer.errors, status=400)


def final_password(request):
    return render(request, "final_password.html")