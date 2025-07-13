from django.urls import path
from .views import ProviderServiceListCreateView, ProviderServiceDetailView,ProviderServicesByServiceId

urlpatterns = [
    path('', ProviderServiceListCreateView.as_view(), name='provider-service-list-create'),
    path('<int:pk>/', ProviderServiceDetailView.as_view(), name='provider-service-detail'),
    path('getProviderlist/<int:service_id>/', ProviderServicesByServiceId.as_view(), name='provider-services-by-service'),
]
