from django import forms
from accounts.models import Email, IthacashUser, IthacashAccount


class EmailForm(forms.ModelForm):

    required_css_class = "required"
    error_css_class = "error"

    class Meta:
        fields = ['address', 'wants_to_receive_updates']
        model = Email
        labels = {
            'address': ''
        }
        widgets = {
            'address': forms.EmailInput(attrs={'placeholder': 'Your email'}),
        }


class AccountForm(forms.ModelForm):

    class Meta:
        model = IthacashAccount
        exclude = ['owner', 'billing_frequency', 'account_type']
        widgets = {
            'entity_name': forms.TextInput(attrs={'placeholder': 'Entity Name'}),
            'address_1': forms.TextInput(attrs={'placeholder': 'Address 1'}),
            'address_2': forms.TextInput(attrs={'placeholder': 'Address 2'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Zip code'}),
            'is_ssn': forms.ChoiceField(widget=forms.RadioSelect, choices=((True, 'SSN'), (False, 'EIN')), initial=False),
            'tin': forms.TextInput(attrs={'placeholder': 'Tax ID #'}, required=False),
            'phone_mobile': forms.TextInput(attrs={'placeholder': 'Mobile Phone'}),
            'phone_landline': forms.TextInput(attrs={'placeholder': 'Contact Phone'}),
            'website': forms.TextInput(attrs={'placeholder': 'Website'}),
            'electronic_signature': forms.TextInput(attrs={'placeholder': 'Your Full Name'})
        }


class UserSignupForm(forms.ModelForm):

    class Meta:
        model = IthacashUser
        fields = ['username', 'full_name']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'})
        }
