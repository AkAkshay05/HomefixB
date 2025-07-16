# invoice/serializers.py
from rest_framework import serializers
from .models import Invoice
from servicerequest.models import ServiceRequest
from servicerequest.serializers import ServiceRequestSerializer

class InvoiceSerializer(serializers.ModelSerializer):
    service_request = ServiceRequestSerializer(read_only=True)  # Nested object
    service_request_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceRequest.objects.all(), write_only=True, source='service_request'
    )

    class Meta:
        model = Invoice
        fields = ['id', 'service_request', 'service_request_id', 'amount', 'description', 'status', 'created_at']

    def validate_status(self, value):
        if value not in ['Accepted', 'Rejected']:
            raise serializers.ValidationError("Status can only be 'Accepted' or 'Rejected'")
        return value