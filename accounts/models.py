from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django import forms
import uuid
from encrypted_fields.fields import EncryptedCharField
import mandrill
from phonenumber_field.modelfields import PhoneNumberField


class IthacashUser(AbstractBaseUser):
    username = models.CharField(max_length=120, unique=True, help_text="Other Ithacash users can use this username to pay you.")
    full_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'


class Email(models.Model):
    address = models.EmailField(unique=True)
    owner = models.ForeignKey(IthacashUser, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    confirmed = models.DateTimeField(blank=True, null=True)
    most_recent_confirmation_key = models.CharField(max_length=255)
    wants_to_receive_updates = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s - %s" % (self.address, self.confirmed or "unconfirmed")

    def save(self, *args, **kwargs):
        if not self.most_recent_confirmation_key:
            self.most_recent_confirmation_key = uuid.uuid4().hex

        return super(Email, self).save(*args, **kwargs)

    def send_confirmation_message(self):

        return
        ## TODO: Email template
        # mandrill_client = mandrill.Mandrill('YOUR_API_KEY')
        # mandrill_client.send(blah blah blah)

    def confirm(self, key):
        if key == self.most_recent_confirmation_key:
            self.confirmed = datetime.now()
            self.save()
            return True
        else:
            return False


class IthacashAccount(models.Model):

    ACCOUNT_TYPE_CHOICES = (
        (None, 'Select Account Type'),
        ('Individual', 'Individual'),
        ('Freelancer', 'Freelancer'),
        ('Standard Business', 'Standard Business'),
        ('Premium Business', 'Premium Business'),
        ('Nonprofit', 'Nonprofit'),
    )

    owner = models.ForeignKey(IthacashUser)

    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    entity_name = models.CharField(max_length=255)

    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, default="Ithaca")
    state = models.CharField(max_length=255, default="NY")
    zip_code = models.CharField(max_length=255, default="14850")
    tin = EncryptedCharField(max_length=255)
    phone_mobile = PhoneNumberField(max_length=255, blank=True, null=True)
    phone_landline = PhoneNumberField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    txt2pay = models.BooleanField()
    txt2pay_phone = models.BooleanField()
    electronic_signature = models.CharField(max_length=5)  # ???

    created = models.DateTimeField(auto_now_add=True)
