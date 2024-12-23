from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from app.organizations.serializers import OrganizationUsersSerializer
from app.organizations.models import Organization

from .serializers import UserSerializer


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