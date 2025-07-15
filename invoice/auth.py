# invoice/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.exceptions import AuthenticationFailed
from serviceprovider.models import ServiceProvider

class ProviderJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            provider_id = validated_token['provider_id']
        except KeyError:
            raise InvalidToken("Token contained no recognizable provider identification")

        try:
            provider = ServiceProvider.objects.get(id=provider_id)
            provider.is_authenticated = True  # ⬅️ Important fix
            return provider
        except ServiceProvider.DoesNotExist:
            raise AuthenticationFailed("Service provider not found")
