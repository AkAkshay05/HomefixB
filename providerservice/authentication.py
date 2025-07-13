from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from serviceprovider.models import ServiceProvider

class ServiceProviderJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        provider_id = validated_token.get("provider_id")
        if not provider_id:
            raise AuthenticationFailed("Invalid token: provider_id not found.")

        try:
            provider = ServiceProvider.objects.get(id=provider_id)
        except ServiceProvider.DoesNotExist:
            raise AuthenticationFailed("ServiceProvider not found.")

        return provider
