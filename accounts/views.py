from django.http.response import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from hendrix.experience import crosstown_traffic
from accounts.models import Email, IthacashUser, IthacashAccount
from signup.models import SignUpForm
from django import forms
from django.db import models


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
        exclude = ['owner']
        widgets = {
            'entity_name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'address_1': forms.TextInput(attrs={'placeholder': 'Address'}),
            'address_2': forms.TextInput(attrs={'placeholder': 'Address'}),
            'city':  forms.TextInput(attrs={'placeholder': 'City'}),
            'state':  forms.TextInput(attrs={'placeholder': 'State'}),
            'zip_code':  forms.TextInput(attrs={'placeholder': 'Zip code'}),
            'tin': forms.TextInput(attrs={'placeholder': 'TIN'}),
            'phone_mobile': forms.TextInput(attrs={'placeholder': 'Mobile Phone'}),
            'phone_landline': forms.TextInput(attrs={'placeholder': 'Contact Phone'}),
            'website': forms.TextInput(attrs={'placeholder': 'Website'}),
            'electronic_signature': forms.TextInput(attrs={'placeholder': 'Electronic Signature'})
        }


class UserSignupForm(forms.ModelForm):

    class Meta:
        model = IthacashUser
        fields = ['username', 'full_name']


def signup_phase_one(request):
    form = EmailForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email_object = form.save()

            @crosstown_traffic()
            def send_email_later():
                email_object.send_confirmation_message()

            return HttpResponseRedirect('/accounts/await-confirmation/')

        else:
            return (JsonResponse({'errors': form.errors.as_json()}))

    else:
        return render(request, 'signup-phase-one.html', {'form': form})

def signup_phase_two(request):
    form = AccountForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email_object = form.save()

            @crosstown_traffic()
            def send_email_later():
                email_object.send_confirmation_message()

            return HttpResponseRedirect('/accounts/purchase-ithaca-dollars/')

        else:
            return (JsonResponse({'errors': form.errors.as_json()}))

    else:
        return render(request, 'signup-phase-two.html', {'form': form})

def await_confirmation(request):
    return render(request, 'await-confirmation.html')


def purchase_ithaca_dollars(request):
    return render(request, 'purchase-ithaca-dollars.html')


def create_account(request, email_key):

    email_object = get_object_or_404(Email, most_recent_confirmation_key=email_key)
    email_object.confirm(email_key)

    user_form = UserSignupForm(request.POST, prefix="user")
    account_form = AccountForm(request.POST, prefix="account")

    if user_form.is_valid() and account_form.is_valid():
        user = user_form.save()

        email_object.owner = user
        email_object.save()

        account_form.instance.owner = user
        account_form.save()

        # Send "Thank you; we'll review your application" email here?

        return HttpResponseRedirect('/accounts/application_complete/')

    return render(request, 'signup-phase-two.html', {'account_form': account_form,
                                                     'user_form': user_form,
                                                     'email_object': email_object})


# TODO: PERMISSIONS!
def list_accounts(request):
    return render(request, 'list-accounts.html', {'accounts': IthacashAccount.objects.all()})
