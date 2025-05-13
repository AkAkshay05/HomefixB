from rest_framework import generics, permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from customers.models import Customer
from rest_framework_simplejwt.exceptions import InvalidToken


class CustomerJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            customer_id = validated_token['customer_id']
        except KeyError:
            raise InvalidToken("Token contained no recognizable customer identification")

        try:
            return Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            raise AuthenticationFailed("Customer not found")

class ServiceRequestListCreateView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    authentication_classes = [CustomerJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        customer = self.request.user
        serializer.save(customer=customer)

class ServiceRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    authentication_classes = [CustomerJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user)
