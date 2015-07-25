from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django import forms
import uuid
from encrypted_fields.fields import EncryptedCharField
import mandrill
from phonenumber_field.modelfields import PhoneNumberField
from ithacash_dev.sayings import USERNAME_DESCRIPTION, DOMAIN, APPLICATION_SUBJECT
from django.template import Context, loader


class IthacashUser(AbstractBaseUser):
    username = models.CharField(max_length=120, unique=True, help_text=USERNAME_DESCRIPTION)
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

    def validate_unique(self, exclude=None):
        try:
            super(Email, self).validate_unique(exclude)
        except ValidationError as e:
            try:
                if e.args[0].keys() == ['address'] and e.args[0]['address'][0].args[1] == 'unique':
                    # In this scenario, the email is a repeat on a form.  It's OK.
                    return
                else:
                    raise
            except:
                raise

    def application_url(self):
        return reverse("account_application", kwargs={'email_key': self.most_recent_confirmation_key})

    def send_confirmation_message(self):
        t = loader.get_template('emails/phase_one.txt')
        c = Context({
            'application_url': "https://%s%s" % (DOMAIN, self.application_url()),
            'form_url': "https://%s%s" % (DOMAIN, reverse("signup_phase_one")),
            'email_address': self.address,
        })
        message = t.render(c)

        mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
        mandrill_client.messages.send(
            {
                'to': [{'email': self.address}],
                'text': message,
                'from_email': 'support@ithacash.com',
                'subject': APPLICATION_SUBJECT,
            })

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
