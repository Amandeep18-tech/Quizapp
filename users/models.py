from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    results = models.CharField(max_length=200, default=" ")

    def __str__(self):
        return f'{self.user.username} Profile'
