from rest_framework import serializers
from .models import ServiceRequest
from serviceprovider.serializers import ServiceProviderSerializer
from customers.serializers import CustomerSerializer
from providerservice.serializers import ProviderServiceSerializer

class ServiceRequestSerializer(serializers.ModelSerializer):
    # Optional: Nested read-only serializers for display purposes
    customer = CustomerSerializer(read_only=True)
    provider = ServiceProviderSerializer(read_only=True)
    service = ProviderServiceSerializer(read_only=True)

    # Accept only the IDs for provider and service on write
    provider_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceRequest._meta.get_field('provider').related_model.objects.all(),
        source='provider',
        write_only=True
    )
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceRequest._meta.get_field('service').related_model.objects.all(),
        source='service',
        write_only=True
    )

    class Meta:
        model = ServiceRequest
        fields = [
            'id',
            'customer',
            'provider',
            'service',
            'provider_id',
            'service_id',
            'schedule_date',
            'schedule_time',
            'address',
            'description',
            'urgency',
            'notes',
            'status',
            'created_at'
        ]
        read_only_fields = ['id', 'customer', 'status', 'created_at', 'provider', 'service']

