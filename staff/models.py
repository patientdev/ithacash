from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class StaffManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=email, password=password)
        user.is_staff = True
        user.save()

        return user

    def create_superuser(self, email, password):
        user = self.model(email=email, password=password)
        user.is_superuser = True
        user.save()

        return user


class IthacashStaff(AbstractBaseUser):
    objects = StaffManager()

    email = models.EmailField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def natural_key(self):
        return (self.email)
