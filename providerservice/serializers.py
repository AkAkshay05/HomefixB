from rest_framework import serializers
from .models import ProviderService

class ProviderServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderService
        fields = '__all__'
        read_only_fields = ['provider']  # Prevent provider from being sent manually
