from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CommentsSerializer
from .models import Comments
# Create your views here.
class CommentsView(viewsets.ModelViewSet):       # add this
  serializer_class = CommentsSerializer          # add this
  queryset = Comments.objects.all()              # add this