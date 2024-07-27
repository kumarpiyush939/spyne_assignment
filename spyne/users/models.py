# from django.db import models

# # from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# class SpyneUser(models.Model):
#     name = models.CharField(max_length=100)
#     mobile_no = models.CharField(max_length=15, unique=True)
#     email = models.EmailField(unique=True)

# # class User(AbstractUser):
# #     mobile_no = models.CharField(max_length=15, unique=True)
# #     email = models.EmailField(unique=True)

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, name, email, mobile_no, password=None, **extra_fields):
        if not name:
            raise ValueError("The Name field must be set")
        if not email:
            raise ValueError("The Email field must be set")
        if not mobile_no:
            raise ValueError("The Mobile number field must be set")

        email = self.normalize_email(email)
        user = self.model(name=name, email=email, mobile_no=mobile_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, mobile_no, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(name, email, mobile_no, password, **extra_fields)


class SpyneUser(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15, unique=True)
    # password = models.CharField(max_length=128, )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['mobile_no', 'name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
