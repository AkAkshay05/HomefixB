from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'service_request', 'amount', 'description', 'status', 'created_at']
        read_only_fields = ['id', 'created_at', 'status']
