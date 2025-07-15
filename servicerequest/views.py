from rest_framework import generics, permissions, status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now

from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from customers.models import Customer

# Custom JWT Authentication for Customers
class CustomerJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            customer_id = validated_token['customer_id']
        except KeyError:
            raise InvalidToken("Token did not contain a valid 'customer_id'")

        try:
            return Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            raise AuthenticationFailed("Customer not found")

# Customer's Service Request View (List + Create)
class ServiceRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = ServiceRequestSerializer
    authentication_classes = [CustomerJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        customer = self.request.user

        schedule_date = serializer.validated_data.get('schedule_date')
        if schedule_date < now().date():
            raise ValidationError({"schedule_date": "Scheduled date cannot be in the past."})

        service = serializer.validated_data.get('service')
        if not service:
            raise ValidationError({"service": "A valid service must be selected."})

        serializer.save(customer=customer)

# Detail View for a Single Service Request (Retrieve / Update / Delete)
class ServiceRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    authentication_classes = [CustomerJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensures customer can only access their own requests
        return ServiceRequest.objects.filter(customer=self.request.user)

# View to Get All Requests for a Specific Provider
class ProviderServiceRequestsView(APIView):
    def get(self, request, provider_id):
        requests = ServiceRequest.objects.filter(provider_id=provider_id)
        if not requests.exists():
            return Response({"detail": "No service requests found for this provider."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceRequestSerializer(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
