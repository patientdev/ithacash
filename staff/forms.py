from django.contrib.auth.forms import AuthenticationForm
from .models import IthacashStaff
from django import forms


class StaffLogin(AuthenticationForm):
    class Meta:
        model = IthacashStaff
        fields = ['email', 'password']


class StaffSignup(forms.ModelForm):

    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput, help_text=("Enter the same password as above, for verification."))

    class Meta:
        model = IthacashStaff
        fields = ['email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(StaffSignup, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user