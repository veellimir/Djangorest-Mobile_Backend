from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import BaseSerializer

from .serializers import (
    OrganizationSerializer,
    OrganizationCurrentUserSerializer
)
from app.users.serializers import UserSerializer

from .models import Organization


class OrganizationCreateView(generics.CreateAPIView):
    serializer_class: type[BaseSerializer] = OrganizationSerializer

    def perform_create(self, serializer: BaseSerializer) -> None:
        serializer.save(owner=self.request.user)


class OrganizationListView(generics.ListAPIView):
    serializer_class: type[BaseSerializer] = OrganizationCurrentUserSerializer

    def get_queryset(self):
        return Organization.objects.filter(members=self.request.user)


class OrganizationUsersView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            return Response({'detail': 'Authentication required'}, status=401)

        organizations = Organization.objects.filter(members=user)
        users = User.objects.filter(organizations__in=organizations).distinct()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)