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

    is_ssn = forms.ChoiceField(widget=forms.RadioSelect, choices=((True, 'SSN'), (False, 'EIN')), required=False)

    class Meta:
        model = IthacashAccount
        exclude = ['owner', 'billing_frequency']
        widgets = {
            'entity_name': forms.TextInput(attrs={'placeholder': 'Entity Name'}),
            'address_1': forms.TextInput(attrs={'placeholder': 'Address 1'}),
            'address_2': forms.TextInput(attrs={'placeholder': 'Address 2'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Zip code'}),
            'tin': forms.TextInput(attrs={'placeholder': 'Tax ID #'}),
            'phone_mobile': forms.TextInput(attrs={'placeholder': 'Mobile Phone'}),
            'phone_landline': forms.TextInput(attrs={'placeholder': 'Contact Phone'}),
            'website': forms.TextInput(attrs={'placeholder': 'Website'}),
            'electronic_signature': forms.TextInput(attrs={'placeholder': 'Your Full Name'})
        }

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)

        if self.instance.account_type == 'Individual':
            self.instance.tin = None
            self.fields['tin'].required = False

    def clean(self):
        cleaned_data = super(AccountForm, self).clean()

        if self.fields['tin'].required:
            tin = cleaned_data.get('tin')

            try:
                int(tin)

            except ValueError:
                raise forms.ValidationError({'tin': ["Please use only numbers", ]})

            except TypeError:
                pass

        return cleaned_data


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
