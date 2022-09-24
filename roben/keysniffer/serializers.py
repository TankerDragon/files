from dataclasses import field
from rest_framework.serializers import ModelSerializer
# models 
from .models import Log

class LogSerializer(ModelSerializer):
    class Meta:
        model = Log
        fields = ['data', 'is_overloaded']