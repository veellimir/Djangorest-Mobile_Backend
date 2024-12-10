from rest_framework import serializers

from .models import CardItem


class CardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardItem
        fields = (
            "id",
            "name",
            "description",
            "price",
            "image",
            "is_available",
        )