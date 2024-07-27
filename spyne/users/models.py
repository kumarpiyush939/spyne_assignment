from django.db import models

# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class SpyneUser(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

# class User(AbstractUser):
#     mobile_no = models.CharField(max_length=15, unique=True)
#     email = models.EmailField(unique=True)
