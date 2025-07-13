from rest_framework import generics, permissions
from .models import ProviderService
from .serializers import ProviderServiceSerializer
from serviceprovider.models import ServiceProvider
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# class ProviderServiceListCreateView(generics.ListCreateAPIView):
#     queryset = ProviderService.objects.all()
#     serializer_class = ProviderServiceSerializer
#     permission_classes = [permissions.IsAuthenticated]

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import ProviderService
from .serializers import ProviderServiceSerializer
from serviceprovider.models import ServiceProvider
from .authentication import ServiceProviderJWTAuthentication
class ProviderServiceListCreateView(generics.ListCreateAPIView):
    queryset = ProviderService.objects.all()
    serializer_class = ProviderServiceSerializer
    authentication_classes = [ServiceProviderJWTAuthentication]
    permission_classes = []  # Optional: or keep IsAuthenticated

    def perform_create(self, serializer):
        provider = self.request.user  # From custom authentication
        serializer.save(provider=provider)




class ProviderServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProviderService.objects.all()
    serializer_class = ProviderServiceSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProviderServicesByServiceId(APIView):
    def get(self, request, service_id):
        providerservices = ProviderService.objects.filter(service_id=service_id)
        serializer = ProviderServiceSerializer(providerservices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)