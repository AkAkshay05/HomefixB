from django.urls import path
from .views import AdminRegisterView, AdminLoginView, AdminDetailView

urlpatterns = [
    path('register/', AdminRegisterView.as_view(), name='admin-register'),
    path('login/', AdminLoginView.as_view(), name='admin-login'),
    path('profile/', AdminDetailView.as_view(), name='admin-profile'),
]
