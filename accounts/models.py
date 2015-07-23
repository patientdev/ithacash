from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
import uuid
import mandrill


class IthacashUser(AbstractBaseUser):
    username = models.CharField(max_length=120, unique=True)

    USERNAME_FIELD = 'username'


class Email(models.Model):
    address = models.EmailField(unique=True)
    owner = models.ForeignKey(IthacashUser, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    confirmed = models.DateTimeField(blank=True, null=True)
    most_recent_confirmation_key = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.most_recent_confirmation_key:
            self.most_recent_confirmation_key = uuid.uuid4().hex

        return super(Email, self).save(*args, **kwargs)

    def send_confirmation_message(self):


        ## TODO: Email template
        mandrill_client = mandrill.Mandrill('YOUR_API_KEY')
        mandrill_client.send(blah blah blah)



    def confirm(self, key):
        if key == self.most_recent_confirmation_key:
            self.confirmed == datetime.now()
            return True
        else:
            return False



