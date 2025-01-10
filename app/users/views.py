from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from app.organizations.serializers import OrganizationUsersSerializer
from app.organizations.models import Organization

from .serializers import UserSerializer, UserPasswordSerializer


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
            raise NotFound("Организация не найдена или вы не состоите в ней.")
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
            return Response(
                {"error": "Неверный текущий пароль, или новый пароль не совпадает"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()

        return Response({"message": "Пароль успешно изменен."}, status=status.HTTP_200_OK)


class UserDeleteAPIView(APIView):
    def delete(self, request):
        user = request.user
        if user.is_authenticated:
            user.delete()
            return Response(
                {"message": "User deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {"error": "User not authenticated"},
                status=status.HTTP_401_UNAUTHORIZED
            )
