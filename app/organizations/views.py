from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import BaseSerializer
from rest_framework import status

from .serializers import (
    OrganizationSerializer,
    OrganizationCurrentUserSerializer,
    OrganizationInviteSerializer
)
from app.users.serializers import UserSerializer

from .models import Organization, OrganizationInvite


class OrganizationCreateView(generics.CreateAPIView):
    serializer_class: type[BaseSerializer] = OrganizationSerializer

    def perform_create(self, serializer: BaseSerializer) -> None:
        serializer.save(owner=self.request.user)


class OrganizationInviteView(generics.CreateAPIView):
    serializer_class: type[OrganizationInviteSerializer] = OrganizationInviteSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrganizationInviteSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            organization_id = serializer.validated_data['organization_id']

            try:
                organization = Organization.objects.get(id=organization_id)
            except Organization.DoesNotExist:
                return Response({"detail": "Организация не найдена."}, status=status.HTTP_404_NOT_FOUND)

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({"detail": "Пользователь с таким username не найден."},
                                status=status.HTTP_404_NOT_FOUND)

            if organization.members.filter(id=user.id).exists():
                return Response({"detail": "Этот пользователь уже является участником организации."},
                                status=status.HTTP_409_CONFLICT)

            # Создаем приглашение
            invite = OrganizationInvite.objects.create(
                organization=organization,
                email=user.email,
                invite=request.user,
                invite_status=OrganizationInvite.ACCEPTED
            )

            organization.members.add(user)

            return Response({
                "detail": f"Пользователь {username} успешно добавлен в организацию '{organization.name}'.",
                "invite_id": invite.id
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
