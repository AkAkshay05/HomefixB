from django.urls import path
from .views import InvoiceListCreateView, InvoiceDetailView,CustomerInvoicesView, InvoiceStatusUpdateView

urlpatterns = [
    path('', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('customer-invoices', CustomerInvoicesView.as_view(), name='customer-invoices'),
    path('update-status/<int:pk>/', InvoiceStatusUpdateView.as_view(), name='update-invoice-status'),
]
