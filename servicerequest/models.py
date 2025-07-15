from django.db import models
from customers.models import Customer
from serviceprovider.models import ServiceProvider
from providerservice.models import ProviderService


class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    service = models.ForeignKey(ProviderService, on_delete=models.CASCADE)

    schedule_date = models.DateField()
    schedule_time = models.TimeField(null=True, blank=True)  # New field for time

    address = models.TextField(blank=True)  # Service address
    description = models.TextField(blank=True)  # Service description

    URGENCY_LEVELS = [
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
        ('emergency', 'Emergency'),
    ]
    urgency = models.CharField(max_length=10, choices=URGENCY_LEVELS, default='normal')

    notes = models.TextField(blank=True)  # Additional notes

    status = models.CharField(max_length=50, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)  # optional timestamp

    def __str__(self):
        return f"{self.customer.username} -> {self.service.name} on {self.schedule_date} at {self.schedule_time or 'N/A'}"

# from django.db import models
# from customers.models import Customer
# from serviceprovider.models import ServiceProvider
# from providerservice.models import ProviderService
#
# class ServiceRequest(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
#     service = models.ForeignKey(ProviderService, on_delete=models.CASCADE)
#     schedule_date = models.DateField()
#     status = models.CharField(max_length=50, default='Pending')
#
#     def __str__(self):
#         return f"{self.customer.username} -> {self.service.name} on {self.schedule_date}"
