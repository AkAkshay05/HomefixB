from rest_framework import generics, permissions
from .models import ServiceProvider
from .serializers import ServiceProviderSerializer

class ServiceProviderListCreateView(generics.ListCreateAPIView):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer


class ServiceProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer
    # permission_classes = [permissions.IsAuthenticated]


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
# from .models import ServiceProvider
# from django.contrib.auth.hashers import check_password
# from datetime import timedelta
# from django.conf import settings
#
# class ServiceProviderLoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#
#         try:
#             provider = ServiceProvider.objects.get(username=username)
#         except ServiceProvider.DoesNotExist:
#             return Response({'error': 'Invalid username'}, status=status.HTTP_401_UNAUTHORIZED)
#
#         if check_password(password, provider.password):
#             # Create tokens manually and embed the provider_id
#             refresh = RefreshToken()
#             refresh['provider_id'] = provider.id
#
#             access = AccessToken()
#             access.set_exp(lifetime=timedelta(minutes=60))  # Optional: set expiry
#             access['provider_id'] = provider.id
#
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(access),
#                 'provider_id': provider.id,
#             })
#
#         return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from datetime import timedelta
from django.contrib.auth.hashers import check_password
from .models import ServiceProvider  # Make sure this is your correct model

class ServiceProviderLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            provider = ServiceProvider.objects.get(username=username)
        except ServiceProvider.DoesNotExist:
            return Response({'error': 'Invalid username'}, status=status.HTTP_401_UNAUTHORIZED)

        if check_password(password, provider.password):
            # ✅ Manually generate JWT tokens (without tying to Django user)
            refresh = RefreshToken()
            refresh.set_exp(lifetime=timedelta(days=1))
            refresh['provider_id'] = provider.id

            access = AccessToken()
            access.set_exp(lifetime=timedelta(minutes=60))
            access['provider_id'] = provider.id

            return Response({
                'refresh': str(refresh),
                'access': str(access),
                'provider_id': provider.id,
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)


