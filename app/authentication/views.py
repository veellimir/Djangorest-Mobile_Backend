from django.contrib.auth.models import User

from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer

from utils.exceptions import EXCEPTION_CONFLICT_USERNAME, EXCEPTION_CONFLICT_EMAIL


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            raise EXCEPTION_CONFLICT_USERNAME

        if User.objects.filter(email=email).exists():
            raise EXCEPTION_CONFLICT_EMAIL

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Пользователь успешно зарегистрирован, теперь вы можете войти"},
            status=status.HTTP_201_CREATED
        )



