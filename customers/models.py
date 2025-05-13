from django.db import models
from django.contrib.auth.hashers import make_password

class Customer(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Only hash password if it's not already hashed
        if not self.pk or not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False
