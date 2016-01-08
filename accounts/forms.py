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
        exclude = ['owner', 'billing_frequency']
        widgets = {
            'entity_name': forms.TextInput(attrs={'placeholder': 'Entity Name', 'required': False}),
            'address_1': forms.TextInput(attrs={'placeholder': 'Address 1'}),
            'address_2': forms.TextInput(attrs={'placeholder': 'Address 2'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Zip code'}),
            'tin': forms.TextInput(attrs={'placeholder': 'Tax ID #', 'required': False}),
            'phone_mobile': forms.TextInput(attrs={'placeholder': 'Mobile Phone'}),
            'phone_landline': forms.TextInput(attrs={'placeholder': 'Contact Phone'}),
            'website': forms.TextInput(attrs={'placeholder': 'Website'}),
            'electronic_signature': forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
            'is_ssn': forms.RadioSelect(attrs={'required': False})
        }

    def clean(self):
        cleaned_data = super(AccountForm, self).clean()
        account_type = cleaned_data.get('account_type')
        entity_name = cleaned_data.get('entity_name')
        tin = cleaned_data.get('tin')
        is_ssn = cleaned_data.get('is_ssn')
        txt2pay = cleaned_data.get('txt2pay')
        txt2pay_phone = cleaned_data.get('txt2pay_phone')
        phone_mobile = cleaned_data.get('phone_mobile')

        if account_type != 'Individual' and (not entity_name or not tin or not is_ssn):
            if not entity_name:
                self.add_error('entity_name', "This field is required.")

            if not tin:
                self.add_error('tin', "This field is required.")

            if not is_ssn:
                self.add_error('is_ssn', "This field is required.")

        if txt2pay and not phone_mobile and not txt2pay_phone:
            self.add_error('phone_mobile', "This field is required to use TXT2PAY")

        return cleaned_data

    def clean_tin(self):
        tin = self.cleaned_data.get('tin', False)

        if tin:
            try:
                int(tin)

            except ValueError as e:
                print e
                self.add_error('tin', 'Please use only numbers')

            except TypeError as e:
                print e

        return tin


class UserSignupForm(forms.ModelForm):

    class Meta:
        model = IthacashUser
        fields = ['username', 'full_name']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'})
        }


class AccountSelectionForm(forms.ModelForm):

    class Meta:
        model = IthacashAccount
        fields = ['account_type']
        widgets = {'account_type': forms.RadioSelect}

    def __init__(self, *args, **kwargs):
        super(AccountSelectionForm, self).__init__(*args, **kwargs)

        for key in self.fields.keys():
            if key is not "account_type":
                self.fields[key].required = False

    def save(self, *args, **kwargs):
        for key in self.fields.keys():
            if key is not "account_type":
                self.fields[key].required = False

        super(AccountSelectionForm, self).save(*args, **kwargs)
