from operator import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model 

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_poster = models.TextField(null=True)