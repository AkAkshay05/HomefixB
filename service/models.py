from django.db import models
from category.models import Category  # Adjust import if needed

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    service_name = models.CharField(max_length=100)

    def __str__(self):
        return self.service_name
