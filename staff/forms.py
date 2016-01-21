from django.contrib.auth.forms import AuthenticationForm
from .models import IthacashStaff
from django import forms

from django.core.exceptions import ValidationError


class StaffLogin(AuthenticationForm):

    username = forms.CharField(label=(""), widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label=(""), widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = IthacashStaff
        fields = ['email', 'password']


class StaffSignup(forms.ModelForm):

    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=(""), widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label=(""), widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Your Password'}), help_text=("Enter the same password as above, for verification."))

    class Meta:
        model = IthacashStaff
        fields = ['email', 'password1', 'password2']
        labels = {
            'email': '',
            'password1': '',
            'password2': ''
        }
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'})
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_domain = email.split('@')[1]

        if email_domain != 'ithacash.com':
            raise ValidationError('You must use an ithacash.com email address. Please contact support@ithacash.com if you require one.')

        return email

    def save(self, commit=True):
        user = super(StaffSignup, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
