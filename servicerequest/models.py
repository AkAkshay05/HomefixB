from django.db import models
from customers.models import Customer
from serviceprovider.models import ServiceProvider
from providerservice.models import ProviderService

class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    service = models.ForeignKey(ProviderService, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.customer.username} -> {self.service.name} on {self.schedule_date}"
