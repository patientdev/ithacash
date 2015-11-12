from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class IthacashStaff(AbstractBaseUser):
    email = models.EmailField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
