from operator import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model 

class User(AbstractUser):
    profile_img=models.TextField(max_length=50000, blank=True)
