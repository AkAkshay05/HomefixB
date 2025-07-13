"""
URL configuration for HomeFixIt project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/customers/', include('customers.urls')),
    path('api/admin/', include('adminManage.urls')),
    path('api/category/', include('category.urls')),
    path('api/service/', include('service.urls')),
    path('api/serviceprovider/', include('serviceprovider.urls')),
    path('api/provider-services/', include('providerservice.urls')),
    path('api/service-requests/', include('servicerequest.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
