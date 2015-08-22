from django import forms

class newsletter_subscription_form(forms.Form):

	auto_id = False

	subscriber_first_name =  forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
	subscriber_last_name =  forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
	subscriber_email_address = forms.EmailField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))

class send_message_form(forms.Form):

	message_from = forms.EmailField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))

	message = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'Name'}))