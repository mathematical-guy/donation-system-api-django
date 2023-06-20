from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    otp = models.CharField(null=True, blank=True, max_length=12)
    contact_number = models.CharField(max_length=24)

    def __str__(self):
        return self.username
