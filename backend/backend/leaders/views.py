from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LeadersSerializer
from .models import Leaders
# Create your views here.

class LeadersView(viewsets.ModelViewSet):
    serializer_class = LeadersSerializer
    queryset = Leaders.objects.all()