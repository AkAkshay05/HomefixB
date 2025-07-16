# invoice/authentication.py

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.exceptions import AuthenticationFailed
from serviceprovider.models import ServiceProvider
from customers.models import Customer

class ProviderJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            provider_id = validated_token['provider_id']
        except KeyError:
            raise InvalidToken("Token contained no recognizable provider identification")

        try:
            provider = ServiceProvider.objects.get(id=provider_id)
            return provider  # ✅ Do NOT set provider.is_authenticated
        except ServiceProvider.DoesNotExist:
            raise AuthenticationFailed("Service provider not found")

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
