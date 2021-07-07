from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    avatar = models.ImageField()

    def __str__(self):
        return str(self.user)
