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
	email_confirm = models.EmailField(max_length=255)
	address_1 = models.CharField(max_length=255, blank=True)
	address_2 = models.CharField(max_length=255, blank=True)
	city =models.CharField(max_length=255, blank=True, default="Ithaca")
	state = models.CharField(max_length=255, blank=True, default="NY")
	zip_code = models.CharField(max_length=255, blank=True, default="14850")
	tin_last4 = models.IntegerField()
	tin = EncryptedCharField(max_length=255)
	landline_phone = models.CharField(max_length=255, blank=True)
	mobile_phone = models.CharField(max_length=255, blank=True)
	website = models.URLField(max_length=255, blank=True)
	referrer = models.CharField(max_length=255, blank=True)
	about = models.TextField(max_length=255, blank=True)
	txt2pay = models.BooleanField()
	txt2pay_phone = models.BooleanField()
	electronic_signature = models.CharField(max_length=5)

class SignUpForm(ModelForm):

	error_css_class = 'error'
	required_css_class = 'required'

	auto_id = False

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		# Placeholders
		self.fields['login_name'].widget.attrs['placeholder'] = 'Username'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['email_confirm'].widget.attrs['placeholder'] = 'Confirm Email'
		self.fields['company_name'].widget.attrs['placeholder'] = 'Business Name'
		self.fields['contact_name'].widget.attrs['placeholder'] = 'Contact Name'
		self.fields['tin'].widget.attrs['placeholder'] = 'Tax ID'
		self.fields['address_1'].widget.attrs['placeholder'] = 'Business Address'
		self.fields['address_2'].widget.attrs['placeholder'] = 'Business Address'
		self.fields['city'].widget.attrs['placeholder'] = 'City'
		self.fields['state'].widget.attrs['placeholder'] = 'State'
		self.fields['zip_code'].widget.attrs['placeholder'] = 'Zip Code'
		self.fields['landline_phone'].widget.attrs['placeholder'] = 'Contact Number'
		self.fields['mobile_phone'].widget.attrs['placeholder'] = 'Mobile Number'
		self.fields['electronic_signature'].widget.attrs['placeholder'] = 'Electronic Signature'

		# Required attributes
		self.fields['account_type'].widget.attrs['required'] = True
		self.fields['company_name'].widget.attrs['required'] = True
		self.fields['contact_name'].widget.attrs['required'] = True
		self.fields['login_name'].widget.attrs['required'] = True
		self.fields['email'].widget.attrs['required'] = True
		self.fields['email_confirm'].widget.attrs['required'] = True
		self.fields['tin'].widget.attrs['required'] = True
		self.fields['address_1'].widget.attrs['required'] = True
		self.fields['landline_phone'].widget.attrs['required'] = True
		self.fields['electronic_signature'].widget.attrs['required'] = True

		self.fields['tin'].label = "EIN/SSN"

	class Meta:
		model = SignUp
		exclude = ['tin_last4']
		labels = {
			'login_name': False,
			'email': False,
			'email_confirm': False,
			'account_type': False,
			'company_name': False,
			'contact_name': False,
			'mobile_phone': False,
			'landline_phone': False,
			'address_1': False,
			'address_2': False,
			'city': False,
			'state': False,
			'zip_code': False,
			'tin' : False
		}
