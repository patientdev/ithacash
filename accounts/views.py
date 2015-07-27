import json
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from hendrix.experience import crosstown_traffic
from django import forms

from accounts.models import Email, IthacashUser, IthacashAccount
from ithacash_dev.sayings import EMAIL_ALREADY_IN_SYSTEM


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
            'entity_name': forms.TextInput(attrs={'placeholder': 'Entity Name'}),
            'address_1': forms.TextInput(attrs={'placeholder': 'Address 1'}),
            'address_2': forms.TextInput(attrs={'placeholder': 'Address 1'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Zip code'}),
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
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            }


def signup_phase_one(request):
    form = EmailForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email_object, created = Email.objects.get_or_create(address=request.POST['address'])

            if email_object.owner:
                return (JsonResponse({'errors': {'address': EMAIL_ALREADY_IN_SYSTEM}}))

            @crosstown_traffic()
            def send_email_later():
                email_object.send_confirmation_message()

            return HttpResponseRedirect('/accounts/await-confirmation/')
        else:
            return (JsonResponse({'errors': form.errors.as_json()}))

    else:
        return render(request, 'signup-phase-one.html', {'form': form})


def await_confirmation(request):
    return render(request, 'await-confirmation.html')


def purchase_ithaca_dollars(request):
    return render(request, 'purchase-ithaca-dollars.html')


def create_account(request, email_key):

    email_object = get_object_or_404(Email, most_recent_confirmation_key=email_key)
    email_object.confirm(email_key)

    user_form = UserSignupForm(request.POST or None)
    account_form = AccountForm(request.POST or None)

    if not request.POST:
        return render(request, 'signup-phase-two.html', {'form': account_form,
                                                     'user_form': user_form,
                                                     'email_object': email_object})

    if user_form.is_valid() and account_form.is_valid():
        user = user_form.save()

        email_object.owner = user
        email_object.save()

        account_form.instance.owner = user
        account_form.save()

        # Send "Thank you; we'll review your application" email here?

        if account_form.cleaned_data['account_type'] is not any(('Individual', 'Nonprofit')):
            return HttpResponseRedirect('/accounts/purchase-ithaca-dollars/')

        else:
            return HttpResponseRedirect('/accounts/sign-up-fee/')

    else:
        # Combine form erros into one payload
        account_errors = json.loads(account_form.errors.as_json())
        user_errors = json.loads(user_form.errors.as_json())
        forms_errors = dict(account_errors.items() + user_errors.items())
        print forms_errors
        return (JsonResponse({'errors': json.dumps(forms_errors)}))


# TODO: PERMISSIONS!
def list_accounts(request):
    return render(request, 'list-accounts.html', {'accounts': IthacashAccount.objects.all()})
