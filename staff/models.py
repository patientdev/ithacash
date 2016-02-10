from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
import mandrill
import uuid
from django.template import Context, loader
from django.utils import timezone
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class IthacashStaffManager(BaseUserManager):

    def create_user(self, email, password):
        email_domain = email.split('@')[1]

        print email_domain

        if email_domain != 'ithacash.com':
            raise ValueError('You must use an ithacash.com email address.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        email_domain = email.split('@')[1]

        if email_domain != 'ithacash.com':
            raise ValueError('You must use an ithacash.com email address.')

        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

    def natural_key(self, email):
        return self.get(email=email)


class IthacashStaff(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    confirmed = models.DateTimeField(blank=True, null=True)
    most_recent_confirmation_key = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = IthacashStaffManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def save(self, *args, **kwargs):
        if not self.most_recent_confirmation_key:
            self.generate_new_confirmation_key()

        return super(IthacashStaff, self).save(*args, **kwargs)

    def generate_new_confirmation_key(self):
        self.most_recent_confirmation_key = uuid.uuid4().hex

    def send_confirmation_message(self):
        t = loader.get_template('emails/phase_one.txt')
        c = Context({
            'application_url': "https://ithacash.com/staff/api/confirm-staff/{}".format(self.most_recent_confirmation_key),
            'form_url': "https://ithacash.com/staff/api/confirm-staff/{}".format(self.most_recent_confirmation_key),
            'email_address': self.email,
        })
        message = t.render(c)

        mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)

        logger.info("Sending confirmation email to %s" % self.email, self)
        mandrill_client.messages.send(
            {
                'to': [{'email': self.email}],
                'text': message,
                'from_name': 'Ithacash Support',
                'from_email': 'support@ithacash.com',
                'subject': 'Confirm your Ithacash Staff account',
            })

    def confirm(self, key):
        if key == self.most_recent_confirmation_key:
            self.confirmed = timezone.now()
            self.save()
            return True
        else:
            return False
