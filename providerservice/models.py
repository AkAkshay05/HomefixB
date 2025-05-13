from django.db import models
from serviceprovider.models import ServiceProvider
from service.models import Service
from django.contrib.auth.models import User
class ProviderService(models.Model):
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.TextField()

    # def __str__(self):
    #     return f"{self.provider.name} - {self.service.ServiceName}"
