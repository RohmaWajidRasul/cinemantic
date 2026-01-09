# Implemented by Rohma
from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    

