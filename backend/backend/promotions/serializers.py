from rest_framework import serializers
from .models import Promotions

class PromotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotions
        fields = ('name', 'image', 'label', 'price', 'featured', 'description')