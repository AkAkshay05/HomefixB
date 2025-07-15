from django.db import models

class ServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    certification = models.CharField(max_length=255)
    average_ratings = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    expertise = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)
    profile_photo = models.ImageField(upload_to='serviceprovider_photos/', null=True, blank=True)  # ✅ New field

    def __str__(self):
        return self.name


