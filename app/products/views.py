from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import CardItem
from .serializers import CardItemSerializer


class CardListView(generics.ListAPIView):
    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer
    permission_classes = [AllowAny]



