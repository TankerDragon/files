from dataclasses import field
from rest_framework.serializers import ModelSerializer
# models 
from .models import Log

class LogSerializer(ModelSerializer):
    class Meta:
        model = Log
        fields = ['data', 'code', 'is_overloaded']

class GetLogSerializer(ModelSerializer):
    class Meta:
        model = Log
        fields = ['id', 'date', 'time', 'data', 'code', 'is_overloaded']