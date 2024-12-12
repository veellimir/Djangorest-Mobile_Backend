from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self) -> Response:
        return self.request.user

