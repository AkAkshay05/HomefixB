from django.urls import path
from .views import ServiceProviderListCreateView, ServiceProviderDetailView
from .views import ServiceProviderLoginView

urlpatterns = [
    path('', ServiceProviderListCreateView.as_view(), name='serviceprovider-list-create'),
    path('<int:pk>/', ServiceProviderDetailView.as_view(), name='serviceprovider-detail'),
    path('login/', ServiceProviderLoginView.as_view(), name='serviceprovider-login'),
]
