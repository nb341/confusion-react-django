from rest_framework import serializers
from .models import Leaders

class LeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaders
        fields = ('name', 'image', 'abbr', 'designation', 'featured', 'description')