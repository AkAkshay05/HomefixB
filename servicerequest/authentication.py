from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from customers.models import Customer

class CustomerJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        customer_id = validated_token.get("customer_id")
        if not customer_id:
            raise AuthenticationFailed("Token missing customer_id")

        try:
            return Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            raise AuthenticationFailed("Customer not found")
