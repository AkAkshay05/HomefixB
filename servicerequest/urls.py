# servicerequest/urls.py
from django.urls import path
from .views import ServiceRequestListCreateView, ServiceRequestDetailView

urlpatterns = [
    path('', ServiceRequestListCreateView.as_view(), name='service-request-list-create'),
    path('<int:pk>/', ServiceRequestDetailView.as_view(), name='service-request-detail'),
]
