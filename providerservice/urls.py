from django.urls import path
from .views import ProviderServiceListCreateView, ProviderServiceDetailView

urlpatterns = [
    path('', ProviderServiceListCreateView.as_view(), name='provider-service-list-create'),
    path('<int:pk>/', ProviderServiceDetailView.as_view(), name='provider-service-detail'),
]
