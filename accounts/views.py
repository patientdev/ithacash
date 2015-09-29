import json
import sys
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from hendrix.experience import crosstown_traffic
from django import forms

from accounts.models import Email, IthacashUser, IthacashAccount
from ithacash_dev.sayings import EMAIL_ALREADY_IN_SYSTEM
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


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

    is_ssn = forms.ChoiceField(widget=forms.RadioSelect, choices=((True, 'SSN'), (False, 'EIN')))

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


class UserSignupForm(forms.ModelForm):

    class Meta:
        model = IthacashUser
        fields = ['username', 'full_name']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'})
        }


class BillingFrequencyForm(forms.ModelForm):

    class Meta:
        model = IthacashAccount
        fields = ['owner', 'billing_frequency']


def getting_an_account(request):
    return render(request, 'getting-an-account.html')


def signup_phase_one(request):
    form = EmailForm(request.POST or None)

    if request.method == 'POST':

        address = request.POST.get('address')

        if form.is_valid():

            if Email.objects.filter(address=address).exists():
                form.add_error('address', EMAIL_ALREADY_IN_SYSTEM)
                return (JsonResponse(form.errors, status=400, reason="BAD REQUEST: Invalid form values"))

            else:
                return (JsonResponse({'success': True}, status=202, reason="OK: Form values accepted"))

        else:
            return (JsonResponse(form.errors, status=400, reason="BAD REQUEST: Invalid form values"))

    else:
        return render(request, 'signup-phase-one.html', {'form': form})


def await_confirmation(request):

    if request.method == 'POST':

        email_object, created = Email.objects.get_or_create(address=request.POST['address'])

        if created:

            @crosstown_traffic()
            def send_email_later():
                email_object.send_confirmation_message()

    return render(request, 'await-confirmation.html')


def purchase_ithaca_dollars(request):
    return render(request, 'purchase-ithaca-dollars.html')


def create_account(request, email_key):

    email_object = get_object_or_404(Email, most_recent_confirmation_key=email_key)
    email_object.confirm(email_key)

    if email_object.owner is not None:

        user_form = UserSignupForm(request.POST or None, instance=IthacashUser.objects.get(username=email_object.owner))
        account_form = AccountForm(request.POST or None, instance=IthacashAccount.objects.get(owner=email_object.owner))
    else:
        user_form = UserSignupForm(request.POST or None)
        account_form = AccountForm(request.POST or None)

    if request.method != 'POST':
        return render(request, 'signup-phase-two.html', {'form': account_form,
                                                         'user_form': user_form,
                                                         'email_object': email_object})

    if user_form.is_valid() and account_form.is_valid():

        # Send "Thank you; we'll review your application" email here?

        if account_form.cleaned_data['account_type'] is 'Individual':
            return HttpResponseRedirect('/accounts/purchase-ithaca-dollars/')

        else:
            return (JsonResponse({'success': True}, status=202, reason="OK: Form values accepted"))

    else:
        # Combine form errors into one payload
        errors = {}
        errors.update(account_form.errors)
        errors.update(user_form.errors)
        return (JsonResponse(errors, status=400, reason="BAD REQUEST: Invalid form values"))


def review(request):

    if request.method == 'POST' and request.POST.get('billing_frequency') is None:

        email_object = Email.objects.get(most_recent_confirmation_key=request.POST['most_recent_confirmation_key'])

        if email_object.owner is not None:
            user_form = UserSignupForm(request.POST or None, instance=IthacashUser.objects.get(username=email_object.owner))
            account_form = AccountForm(request.POST or None, instance=IthacashAccount.objects.get(owner=email_object.owner))
        else:
            user_form = UserSignupForm(request.POST or None)
            account_form = AccountForm(request.POST or None)

        if user_form.is_valid() and account_form.is_valid():

            user = user_form.save()

            account_form.instance.owner = user
            account = account_form.save()

            email_object.owner = user
            email_object.save()

            last_4 = request.POST['tin'][-4:]

            settings.PAYPAL_SETTINGS['button_ids'][account.account_type]

            context = {
                'user': user,
                'account': account,
                'email_object': email_object,
                'last_4': last_4,
                'paypal_form': settings.PAYPAL_SETTINGS,
                'paypal_button_id': settings.PAYPAL_SETTINGS['button_ids'][account.account_type]
            }

            return render(request, 'review.html', context)

        else:
            # Combine form errors into one payload
            errors = {}
            errors.update(account_form.errors)
            errors.update(user_form.errors)
            return (JsonResponse(errors, status=400, reason="BAD REQUEST: Invalid form values"))

    elif request.POST.get('billing_frequency') is not None:

        billing_form = BillingFrequencyForm(request.POST or None)

        ithacash_user = IthacashUser.objects.get(username=request.POST.get('account_owner'))
        ithacash_user.ithacashaccount_set.update(billing_frequency=request.POST['billing_frequency'])

        return JsonResponse({'success': True})

    else:
        return HttpResponseRedirect('/accounts/signup/')


def thanks(request):
    return render(request, 'thanks.html')


def whoops(request):
    return render(request, 'whoops.html')


# TODO: PERMISSIONS!
def list_accounts(request):
    return render(request, 'list-accounts.html', {'accounts': IthacashAccount.objects.all()})
