from rest_framework import generics, permissions, serializers
from .models import Invoice
from .serializers import InvoiceSerializer
from .auth import ProviderJWTAuthentication  # Assuming your custom authentication

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    authentication_classes = [ProviderJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user  # Authenticated provider
        return Invoice.objects.filter(service_request__provider=user)

    def perform_create(self, serializer):
        service_request = serializer.validated_data['service_request']
        if service_request.provider != self.request.user:
            raise serializers.ValidationError("You can only create invoices for your own service requests.")
        serializer.save(status='Sent')


class InvoiceDetailView(generics.RetrieveUpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    authentication_classes = [ProviderJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Invoice.objects.filter(service_request__provider=user)
