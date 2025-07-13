from rest_framework import serializers
from .models import ServiceRequest
from serviceprovider.serializers import ServiceProviderSerializer
from customers.serializers import CustomerSerializer
from providerservice.serializers import ProviderServiceSerializer

class ServiceRequestSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer()
    # service = ProviderServiceSerializer()
    # provider = ServiceProviderSerializer()

    class Meta:
        model = ServiceRequest
        fields = '__all__'
        read_only_fields = ['customer']  # Automatically set from the token
