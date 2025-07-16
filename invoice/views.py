from rest_framework import generics, permissions, serializers
from .models import Invoice
from .serializers import InvoiceSerializer
from .auth import ProviderJWTAuthentication, CustomerJWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from customers.models import Customer
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


class CustomerInvoicesView(APIView):
    authentication_classes = [CustomerJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            customer = Customer.objects.get(id=request.user.id)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer profile not found.'}, status=404)

        invoices = Invoice.objects.filter(service_request__customer=customer).order_by('-created_at')
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

class InvoiceStatusUpdateView(APIView):
    authentication_classes = [CustomerJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        customer = request.user  # ✅ Use this instead of Customer.objects.get(...)

        try:
            invoice = Invoice.objects.get(pk=pk, service_request__customer=customer)
        except Invoice.DoesNotExist:
            return Response({'error': 'Invoice not found for this customer'}, status=404)

        serializer = InvoiceSerializer(invoice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Invoice status updated successfully'})
        return Response(serializer.errors, status=400)
