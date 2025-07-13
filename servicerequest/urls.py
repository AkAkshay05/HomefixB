# servicerequest/urls.py
from django.urls import path
from .views import ServiceRequestListCreateView, ServiceRequestDetailView, ProviderServiceRequestsView

urlpatterns = [
    path('', ServiceRequestListCreateView.as_view(), name='service-request-list-create'),
    path('<int:pk>/', ServiceRequestDetailView.as_view(), name='service-request-detail'),
    path('provider/<int:provider_id>/', ProviderServiceRequestsView.as_view(), name='provider-service-requests'),
]
