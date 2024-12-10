from urllib.request import Request

from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class CardListView(generics.RetrieveAPIView):
    pass
