# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    uid = models.CharField(max_length=100, null=True)
    credits = models.FloatField(default=10)
