from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class AdminManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None):
        if not username:
            raise ValueError("Admin must have a username")
        if not phone_number:
            raise ValueError("Admin must have a phone number")

        admin = self.model(username=username, phone_number=phone_number)
        admin.set_password(password)
        admin.save(using=self._db)
        return admin

    def create_admin(self, username, phone_number, password=None):
        admin = self.create_user(username=username, phone_number=phone_number, password=password)
        admin.is_staff = True  # Admin should have staff privileges
        admin.is_superuser = True  # If applicable
        admin.save(using=self._db)
        return admin

class Admin(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AdminManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return self.username
