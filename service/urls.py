from django.urls import path
from .views import ServiceListCreateView, ServiceDetailView,ServicesByCategoryView

urlpatterns = [
    path('', ServiceListCreateView.as_view(), name='service-list-create'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('by-category/<int:category_id>/', ServicesByCategoryView.as_view(), name='services-by-category'),

]
