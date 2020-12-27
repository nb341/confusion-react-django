from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PromotionsSerializer
from .models import Promotions
# Create your views here.

class PromotionsView(viewsets.ModelViewSet):
    serializer_class = PromotionsSerializer
    queryset = Promotions.objects.all()
