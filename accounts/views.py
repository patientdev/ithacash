import json
import sys
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseServerError
from django.shortcuts import render, get_object_or_404
from hendrix.experience import crosstown_traffic
from django import forms

from accounts.models import Email, IthacashUser, IthacashAccount
<<<<<<< HEAD
from ithacash.sayings import EMAIL_ALREADY_IN_SYSTEM
=======
from ithacash_dev.sayings import EMAIL_ALREADY_IN_SYSTEM
>>>>>>> refs/remotes/origin/master
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.views.decorators.cache import never_cache, cache_control
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

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
        return render(request, 'accounts/signup-step-1-confirm-email.html', {'form': form})


def signup_step_2_await_confirmation(request):

    if request.method == 'POST':

        email_object, created = Email.objects.get_or_create(address=request.POST['address'])

        if created:

            @crosstown_traffic()
            def send_email_later():
                email_object.send_confirmation_message()

            return render(request, 'accounts/signup-step-2-await-confirmation.html')

        else:
            return HttpResponseRedirect('/accounts/signup/')


@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
def signup_step_3_select_account_type(request, email_key):

    email_object = get_object_or_404(Email, most_recent_confirmation_key=email_key)
    email_object.confirm(email_key)

    # Create the user and associated account if newly confirmed
    if email_object.owner is None:
        email_object.owner = IthacashUser.objects.create()
        email_object.save()

    try:
        account = IthacashAccount.objects.get(owner_id=email_object.owner_id)
        account_form = AccountSelectionForm(request.POST or None, instance=account)
    except IthacashAccount.DoesNotExist:
        account_form = AccountSelectionForm(request.POST or None)

    if request.method == 'POST':

        if account_form.is_valid():
            return (JsonResponse({'success': True}, status=202, reason="OK: Form values accepted"))

        else:
            return (JsonResponse(account_form.errors, status=400, reason="BAD REQUEST: Invalid form values"))

    else:
        return render(request, 'accounts/signup-step-3-select-account-type.html', {'form': account_form, 'user_id': email_object.owner_id})

@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
def signup_step_4_account_information(request):

    if request.method == 'POST':

        # Submit account type
        if "validate" not in request.POST:
            user_id = request.POST.get('user_id')

            try:
                account = IthacashAccount.objects.get(owner_id=user_id)
                account_selection_form = AccountSelectionForm(request.POST or None, instance=account)
                account_selection_form.save()
                account_form = AccountForm(instance=account)
            except ObjectDoesNotExist:
                account_selection_form = AccountSelectionForm(request.POST or None)
                account_form = AccountForm(initial={'account_type': request.POST.get('account_type')})

            user_form = UserSignupForm(instance=IthacashUser.objects.get(id=user_id))

            context = {
                'account_form': account_form,
                'user_form': user_form,
                'user_id': user_id
            }

            return render(request, 'accounts/signup-step-4-account-information.html', context)

        # Handle Step 4 validation
        else:
            user_id = request.POST.get('user_id')

            user_object = IthacashUser.objects.get(id=user_id)

            try:
                account = IthacashAccount.objects.get(owner_id=user_id)
                account_form = AccountForm(request.POST, instance=account)
            except ObjectDoesNotExist:
                account_form = AccountForm(request.POST)

            user_form = UserSignupForm(request.POST, instance=user_object)

            if account_form.is_valid() and user_form.is_valid():

                return JsonResponse({'success': True}, status=202, reason="OK: Form values accepted")

            else:
                errors = {}
                errors.update(account_form.errors)
                errors.update(user_form.errors)

                return JsonResponse(errors, status=400, reason="BAD REQUEST: Invalid form values")


@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
def review(request):

    if request.method == 'POST':

        user_id = request.POST.get('user_id')

        user_object = IthacashUser.objects.get(id=user_id)
        email_object = Email.objects.get(owner=user_object)

        try:
            account_object = IthacashAccount.objects.get(owner=user_object)
            account_form = AccountForm(request.POST, instance=account_object)
        except ObjectDoesNotExist:
            account_form = AccountForm(request.POST)

        user_form = UserSignupForm(request.POST, instance=user_object)

        if account_form.is_valid() and user_form.is_valid():

            try:
                account_object = account_form.save(commit=False)
                account_object.owner = user_object
                account_object.save()
                account_form.save_m2m()
            except:
                account_form.save()

            user_form.save()

            context = {
                'user': user_object,
                'account': account_object,
                'email': email_object,
                'paypal_form': settings.PAYPAL_SETTINGS,
                'paypal_button_id': settings.PAYPAL_SETTINGS['button_ids'][account_object.account_type],
                'sign_up_fee': settings.ACCOUNT_PROPERTIES[account_object.account_type]['SIGN_UP_FEE'],
                'monthly_cost': settings.ACCOUNT_PROPERTIES[account_object.account_type]['MONTHLY'],
                'txt2pay_phone_cost': settings.ACCOUNT_PROPERTIES['TXT2PAY_PHONE']
            }

            return render(request, 'accounts/signup-step-5-review.html', context)

        else:
            return HttpResponseServerError()

    else:
        return HttpResponse("Please click the back button to return to the previous page or click the link in your confirmation email and try again.")


def whoops(request):
    return render(request, 'whoops.html')


def purchase_ithaca_dollars(request):
    return render(request, 'purchase-ithaca-dollars.html')


# TODO: PERMISSIONS!
def list_accounts(request):
    return render(request, 'list-accounts.html', {'accounts': IthacashAccount.objects.all()})
