from django.db import models
from django.forms import ModelForm
from encrypted_fields import EncryptedCharField

class SignUp(models.Model):
	ACCOUNT_TYPE_CHOICES = (
		(None, 'Who are you?'),
		('Individual', 'Individual'),
		('Freelancer', 'Freelancer'),
		('Business', 'Business'),
		('Nonprofit', 'Nonprofit'),
	)

	account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
	company_name = models.CharField(max_length=255)
	contact_name = models.CharField(max_length=255)
	login_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	mobile_phone = models.CharField(max_length=255, blank=True)
	landline_phone = models.CharField(max_length=255, blank=True)
	address_1 = models.CharField(max_length=255, blank=True)
	address_2 = models.CharField(max_length=255, blank=True)
	city =models.CharField(max_length=255, blank=True)
	state = models.CharField(max_length=255, blank=True)
	zip_code = models.CharField(max_length=255, blank=True)
	tin_last4 = models.IntegerField()
	tin = EncryptedCharField(max_length=100)
	website = models.URLField(max_length=255, blank=True)
	referrer = models.CharField(max_length=255, blank=True)
	about = models.TextField(max_length=255, blank=True)

class SignUpForm(ModelForm):

	error_css_class = 'error'
	required_css_class = 'required'

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['account_type'].widget.attrs['required'] = True
		self.fields['company_name'].widget.attrs['required'] = True
		self.fields['contact_name'].widget.attrs['required'] = True
		self.fields['login_name'].widget.attrs['required'] = True
		self.fields['email'].widget.attrs['required'] = True

		self.fields['city'].widget.attrs['value'] = 'Ithaca'
		self.fields['state'].widget.attrs['value'] = 'NY'
		self.fields['zip_code'].widget.attrs['value'] = 14850

		self.fields['tin'].label = "EIN/SSN"

	class Meta:
		model = SignUp

		exclude = ['tin_last4']
