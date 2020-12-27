from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import DishesSerializer      # add this
from .models import Dishes
class DishesView(viewsets.ModelViewSet):       # add this
  serializer_class = DishesSerializer          # add this
  queryset = Dishes.objects.all()              # add this
