from rest_framework import generics, permissions
from .models import Service
from .serializers import ServiceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = [permissions.IsAuthenticated]



class ServicesByCategoryView(APIView):
    def get(self, request, category_id):
        services = Service.objects.filter(category_id=category_id)
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
