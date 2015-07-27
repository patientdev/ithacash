from datetime import datetime
from django.db import models
from django import forms
from django.forms import ModelForm
from encrypted_fields import EncryptedCharField
from phonenumber_field.modelfields import PhoneNumberField


class SignUp(models.Model):

    ACCOUNT_TYPE_CHOICES = (
        (None, 'Who are you?'),
        ('Individual', 'Individual'),
        ('Freelancer', 'Freelancer'),
        ('Business', 'Business'),
        ('Nonprofit', 'Nonprofit'),
    )

    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    name_business = models.CharField(max_length=255)
    name_contact = models.CharField(max_length=255)
    name_login = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    address_city = models.CharField(max_length=255, default="Ithaca")
    address_state = models.CharField(max_length=255, default="NY")
    address_zip_code = models.CharField(max_length=255, default="14850")
    tin = EncryptedCharField(max_length=255)
    phone_mobile = PhoneNumberField(max_length=255, blank=True, null=True)
    phone_landline = PhoneNumberField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    txt2pay = models.BooleanField()
    txt2pay_phone = models.BooleanField()
    electronic_signature = models.CharField(max_length=5)  # ???

    created = models.DateTimeField(auto_now_add=True)

    def tin_last4(self):
        return self.tin[-4:]


class SignUpForm(ModelForm):

    error_css_class = 'error'
    # required_css_class = 'required'

    auto_id = False

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Placeholders
        self.fields['name_login'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['name_business'].widget.attrs['placeholder'] = 'Business Name'
        self.fields['name_contact'].widget.attrs['placeholder'] = 'Contact Name'
        self.fields['tin'].widget.attrs['placeholder'] = 'Tax ID'
        self.fields['address_1'].widget.attrs['placeholder'] = 'Business Address'
        self.fields['address_2'].widget.attrs['placeholder'] = 'Business Address'
        self.fields['address_city'].widget.attrs['placeholder'] = 'City'
        self.fields['address_state'].widget.attrs['placeholder'] = 'State'
        self.fields['address_zip_code'].widget.attrs['placeholder'] = 'Zip Code'
        self.fields['phone_landline'].widget.attrs['placeholder'] = 'Contact Number'
        self.fields['phone_mobile'].widget.attrs['placeholder'] = 'Mobile Number'
        self.fields['electronic_signature'].widget.attrs['placeholder'] = 'Electronic Signature'

    class Meta:
        model = SignUp
        exclude = ('account_type',)
        labels = {
            'name_login': False,
            'email': False,
            'name_business': False,
            'name_contact': False,
            'phone_mobile': False,
            'phone_landline': False,
            'address_1': False,
            'address_2': False,
            'address_city': False,
            'address_state': False,
            'address_zip_code': False,
            'tin': False
        }
