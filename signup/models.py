from django.db import models
from django.forms import ModelForm

class SignUp(models.Model):
	ACCOUNT_TYPE_CHOICES = (
		(None, 'Who are you?'),
		('individual', 'Individual'),
		('freelancer', 'Freelancer'),
		('business', 'Business'),
		('nonprofit', 'Nonprofit'),
	)

	account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
	name_company = models.CharField(max_length=255)
	name_contact = models.CharField(max_length=255)
	name_login = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	phone_mobile = models.CharField(max_length=255, blank=True)
	phone_landline = models.CharField(max_length=255, blank=True)
	address_1 = models.CharField(max_length=255, blank=True)
	address_2 = models.CharField(max_length=255, blank=True)
	address_city =models.CharField(max_length=255, blank=True)
	address_state = models.CharField(max_length=255, blank=True)
	address_zip = models.CharField(max_length=255, blank=True)
	website = models.URLField(max_length=255, blank=True)
	referrer =models.CharField(max_length=255, blank=True)
	about =models.TextField(max_length=255, blank=True)

class SignUpForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['account_type'].widget.attrs['required'] = True
		self.fields['name_company'].widget.attrs['required'] = True
		self.fields['name_contact'].widget.attrs['required'] = True
		self.fields['name_login'].widget.attrs['required'] = True
		self.fields['email'].widget.attrs['required'] = True

		self.fields['address_city'].widget.attrs['value'] = 'Ithaca'
		self.fields['address_state'].widget.attrs['value'] = 'NY'
		self.fields['address_zip'].widget.attrs['value'] = 14850

	class Meta:
		model = SignUp

		fields = ['account_type', 'name_company', 'name_contact', 'name_login', 'email', 'phone_mobile', 'phone_landline', 'address_1', 'address_2', 'address_city', 'address_state', 'address_zip', 'website', 'referrer', 'about',]