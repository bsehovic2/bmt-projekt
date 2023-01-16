# entries/models.py

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Entry(models.Model):
    type = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="entries",
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.user.uid

    def get_absolute_url(self) -> object:
        return reverse('post', args=[str(self.id)])

