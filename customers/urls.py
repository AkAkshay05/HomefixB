from django.urls import path
from .views import CustomerListCreateView, CustomerDetailView, CustomerLoginView

urlpatterns = [
    path('', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('login/', CustomerLoginView.as_view(), name='customer-login'),
]
