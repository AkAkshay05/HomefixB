from django.urls import path
from .views import (
    ServiceRequestListCreateView,
    ServiceRequestDetailView,
    ProviderServiceRequestsView,
    CustomerServiceRequestsView
)

urlpatterns = [
    path('', ServiceRequestListCreateView.as_view(), name='service-request-list-create'),
    path('<int:pk>/', ServiceRequestDetailView.as_view(), name='service-request-detail'),
    path('provider/', ProviderServiceRequestsView.as_view(), name='provider-service-requests'),
    path('customer-requests/', CustomerServiceRequestsView.as_view(), name='customer-service-requests'),

]
