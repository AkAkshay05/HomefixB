from rest_framework import serializers
from .models import ProviderService
from service.serializers import ServiceSerializer  # or define it above if same file

class ProviderServiceSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)  # <-- Nest service details

    class Meta:
        model = ProviderService
        fields = '__all__'
        read_only_fields = ['provider', 'id']
