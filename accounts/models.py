from datetime import datetime
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
import uuid
from encrypted_fields.fields import EncryptedCharField
import mandrill
from phonenumber_field.modelfields import PhoneNumberField
from ithacash.sayings import USERNAME_DESCRIPTION, DOMAIN, EMAIL_CONFIMATION_SUBJECT_LINE, VERIFICATION_SUBJECT_LINE
from django.template import Context, loader
from django.conf import settings
from django.core import validators
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class IthacashUser(AbstractBaseUser):
    username = models.CharField(max_length=120, unique=True, null=True, default=None, help_text=USERNAME_DESCRIPTION, validators=[validators.MinLengthValidator(5), validators.RegexValidator(r'^[0-9a-zA-Z]*$', 'Only letters and numbers are allowed')])
    full_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()


class Email(models.Model):
    address = models.EmailField(unique=True)
    owner = models.ForeignKey(IthacashUser, related_name="emails", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    confirmed = models.DateTimeField(blank=True, null=True)
    most_recent_confirmation_key = models.CharField(max_length=255)
    wants_to_receive_updates = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s - %s" % (self.address, self.confirmed or "unconfirmed")

    def save(self, *args, **kwargs):
        if not self.most_recent_confirmation_key:
            self.generate_new_confirmation_key()

        return super(Email, self).save(*args, **kwargs)

    def validate_unique(self, exclude=None):
        try:
            super(Email, self).validate_unique(exclude)
        except ValidationError as e:
            try:
                if e.args[0].keys() == ['address'] and e.args[0]['address'][0].args[1] == 'unique':
                    return
                else:
                    raise
            except:
                raise

    def generate_new_confirmation_key(self):
        self.most_recent_confirmation_key = uuid.uuid4().hex

    def confirmation_url(self):
        return reverse("api_confirm_email", kwargs={'email_key': self.most_recent_confirmation_key})

    def send_confirmation_message(self):
        t = loader.get_template('emails/phase_one.txt')
        c = {
            'confirmation_url': "https://%s%s" % (DOMAIN, self.confirmation_url()),
            'form_url': "https://%s%s" % (DOMAIN, reverse("signup_step_1_confirm_email")),
            'email_address': self.address,
        }
        message = t.render(c)

        mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)

        logger.info("Sending confirmation email to %s" % self.address, self)
        mandrill_client.messages.send(
            {
                'to': [{'email': self.address}],
                'text': message,
                'from_name': 'Ithacash Support',
                'from_email': 'support@ithacash.com',
                'subject': EMAIL_CONFIMATION_SUBJECT_LINE,
            })

    def confirm(self, key):
        if key == self.most_recent_confirmation_key:
            self.confirmed = timezone.now()
            self.save()
            return True
        else:
            return False


class IthacashAccount(models.Model):

    ACCOUNT_TYPE_CHOICES = (
        ('Individual', 'Individual'),
        ('Freelancer', 'Freelancer'),
        ('Standard Business', 'Standard Business'),
        ('Premier Business', 'Premier Business'),
        ('Nonprofit', 'Nonprofit'),
    )

    BILLING_FREQUENCY_CHOICES = (
        ('Monthly', 'Monthly'),
        ('Semi-Annual', 'Semi-Annual')
    )

    owner = models.ForeignKey(IthacashUser, related_name="accounts")

    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    entity_name = models.CharField(max_length=255, blank=True)

    billing_frequency = models.CharField(max_length=11, choices=BILLING_FREQUENCY_CHOICES, default='Monthly')

    address_1 = models.CharField(max_length=255,)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    tin = EncryptedCharField(max_length=255, blank=True, help_text="This is a secure site. Your Tax ID # will not be seen by anyone internally, distributed, or shared.", validators=[validators.MinLengthValidator(9, "This should be exactly 9 numbers. (It has %(show_value)d)"), validators.MaxLengthValidator(9, "This should be exactly 9 numbers. (It has %(show_value)d)")])
    is_ssn = models.BooleanField(default=True, blank=True, choices=((True, 'SSN'), (False, 'EIN')))
    phone_mobile = PhoneNumberField(max_length=255, blank=True)
    phone_landline = PhoneNumberField(max_length=255)
    website = models.URLField(max_length=255, blank=True)
    txt2pay = models.BooleanField(default=False)
    txt2pay_phone = models.BooleanField(default=False)
    electronic_signature = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    registration_complete = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if self.entity_name == '':
            self.entity_name = self.owner.full_name

        return super(IthacashAccount, self).save(*args, **kwargs)

    def send_awaiting_verification_message(self):

        account_email = self.owner.emails.all()[0].address

        t = loader.get_template('emails/please_wait_while_we_verify.txt')
        c = Context({})
        message = t.render(c)

        mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)

        logger.info("Sending verification email to %s for account %s" % (account_email, self))
        message = mandrill_client.messages.send(
            {
                'to': [{'email': account_email}],  # Right now, users aren't allowed to have more than one email address.
                'text': message,
                'from_name': 'Ithacash Support',
                'from_email': 'support@ithacash.com',
                'subject': VERIFICATION_SUBJECT_LINE,
            })
