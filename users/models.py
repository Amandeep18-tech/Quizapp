from django.db import models
import uuid
from django.contrib.auth.models import User


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    results = models.CharField(max_length=200, default="0")

    def __str__(self):
        return f'{self.user.username} Profile'
