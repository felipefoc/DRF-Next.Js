from django.db import models
from django.conf import settings


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    """
    Many other attributes like display_name, dob, hometown, etc
    """
