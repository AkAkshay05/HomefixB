# serviceprovider/authentication.py

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.exceptions import AuthenticationFailed
from serviceprovider.models import ServiceProvider

class ProviderJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            provider_id = validated_token['provider_id']
        except KeyError:
            raise InvalidToken("Token did not contain a valid 'provider_id'")

        try:
            return ServiceProvider.objects.get(id=provider_id)
        except ServiceProvider.DoesNotExist:
            raise AuthenticationFailed("Service provider not found")
