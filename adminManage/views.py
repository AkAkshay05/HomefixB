from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Admin
from .serializers import AdminSerializer

class AdminRegisterView(APIView):
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Admin registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        admin = authenticate(username=username, password=password)  # ✅ Now works correctly
        if admin:
            refresh = RefreshToken.for_user(admin)
            return Response({
                "message": "Login successful",
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class AdminDetailView(APIView):
    def get(self, request):
        admin = request.user
        serializer = AdminSerializer(admin)
        return Response(serializer.data, status=status.HTTP_200_OK)
