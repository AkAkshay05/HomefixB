from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer

# Create and List Customers
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Retrieve, Update, Delete Customer
class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from datetime import timedelta
from django.contrib.auth.hashers import check_password
from .models import Customer  # Assuming you have a custom Customer model

class CustomerLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            customer = Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            return Response({'error': 'Invalid username'}, status=status.HTTP_401_UNAUTHORIZED)

        if check_password(password, customer.password):
            # Create JWT tokens manually
            refresh = RefreshToken()
            refresh.set_exp(lifetime=timedelta(days=1))
            refresh['customer_id'] = customer.id

            access = AccessToken()
            access.set_exp(lifetime=timedelta(minutes=60))
            access['customer_id'] = customer.id

            return Response({
                'refresh': str(refresh),
                'access': str(access),
                'customer_id': customer.id,
            })

        return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

