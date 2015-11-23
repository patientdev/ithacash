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


class AccountSelectionForm(forms.ModelForm):

    class Meta:
        model = IthacashAccount
        fields = ['account_type']


def getting_an_account(request):
    return render(request, 'getting-an-account.html')


def signup_step_1_confirm_email(request):
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
        return render(request, 'signup-step-1-confirm-email.html', {'form': form})


def signup_step_2_await_confirmation(request):

    if request.method == 'POST':

        email_object, created = Email.objects.get_or_create(address=request.POST['address'])

        if created:

            @crosstown_traffic()
            def send_email_later():
                email_object.send_confirmation_message()

            return render(request, 'signup-step-2-await-confirmation.html')

        else:
            return HttpResponseRedirect('/accounts/signup/')


def signup_step_3_select_account_type(request, email_key):

    email_object = get_object_or_404(Email, most_recent_confirmation_key=email_key)
    email_object.confirm(email_key)

    if email_object.owner is None:
        email_object.owner = IthacashUser.objects.create()
        email_object.save()
        IthacashAccount.objects.create(owner=email_object.owner)

    account_form = AccountSelectionForm(request.POST or None, instance=IthacashAccount.objects.get(owner=email_object.owner))

    if request.method == 'POST':

        if account_form.is_valid():
            return (JsonResponse({'success': True}, status=202, reason="OK: Form values accepted"))

        else:
            return (JsonResponse(account_form.errors, status=400, reason="BAD REQUEST: Invalid form values"))

    else:
        return render(request, 'signup-step-3-select-account-type.html', {'form': account_form})


def signup_step_4_account_information(request):

    if request.method == 'POST':
        account_selection_form = AccountSelectionForm(request.POST)
        account = account_selection_form.save(commit=False)
        print account.id
        account_form = AccountForm(instance=IthacashAccount.objects.get(id=account.id))
        user_form = UserSignupForm(instance=IthacashUser.objects.get(id=account.owner_id))
        email_form = EmailForm(instance=Email.objects.get(id=account.owner_id))

        return render(request, 'signup-step-4-account-information.html', {'account_form': account_form, 'user_form': user_form, 'email_form': email_form})


# def review(request):
#
#     if request.method == 'POST' and request.POST.get('billing_frequency') is None:
#
#         email_object = Email.objects.get(most_recent_confirmation_key=request.POST['most_recent_confirmation_key'])
#
#         if email_object.owner is not None:
#             user_form = UserSignupForm(request.POST or None, instance=IthacashUser.objects.get(username=email_object.owner))
#             account_form = AccountForm(request.POST or None, instance=IthacashAccount.objects.get(owner=email_object.owner))
#         else:
#             user_form = UserSignupForm(request.POST or None)
#             account_form = AccountForm(request.POST or None)
#
#         if user_form.is_valid() and account_form.is_valid():
#
#             user = user_form.save()
#
#             account_form.instance.owner = user
#             account = account_form.save()
#
#             email_object.owner = user
#             email_object.save()
#
#             last_4 = request.POST['tin'][-4:]
#
#             context = {
#                 'user': user,
#                 'account': account,
#                 'email_object': email_object,
#                 'last_4': last_4,
#                 'paypal_form': settings.PAYPAL_SETTINGS,
#                 'paypal_button_id': settings.PAYPAL_SETTINGS['button_ids'][account.account_type]
#             }
#
#             return render(request, 'review.html', context)
#
#         else:
#             # Combine form errors into one payload
#             errors = {}
#             errors.update(account_form.errors)
#             errors.update(user_form.errors)
#
#             return (JsonResponse(errors, status=400, reason="BAD REQUEST: Invalid form values"))
#
#     elif request.POST.get('billing_frequency') is not None:
#
#         billing_form = BillingFrequencyForm(request.POST or None)
#
#         ithacash_user = IthacashUser.objects.get(username=request.POST.get('account_owner'))
#         ithacash_user.ithacashaccount_set.update(billing_frequency=request.POST['billing_frequency'])
#
#         return JsonResponse({'success': True})
#
#     else:
#         return HttpResponseRedirect('/accounts/signup/')


def thanks(request):
    return render(request, 'thanks.html')


def whoops(request):
    return render(request, 'whoops.html')


def purchase_ithaca_dollars(request):
    return render(request, 'purchase-ithaca-dollars.html')


# TODO: PERMISSIONS!
def list_accounts(request):
    return render(request, 'list-accounts.html', {'accounts': IthacashAccount.objects.all()})
