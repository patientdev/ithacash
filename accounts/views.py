from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from hendrix.experience import crosstown_traffic
from accounts.models import Email, IthacashUser, IthacashAccount
from signup.models import SignUpForm
from django import forms


class EmailForm(forms.ModelForm):

    class Meta:
        fields = ['address', 'wants_to_receive_updates']
        model = Email


class AccountForm(forms.ModelForm):

    class Meta:
        model = IthacashAccount
        exclude = ['owner']


class UserSignupForm(forms.ModelForm):

    class Meta:
        model = IthacashUser
        fields = ['username', 'full_name']


def signup_phase_one(request):
    form = EmailForm(request.POST)

    if form.is_valid():
        email_object = form.save()

        @crosstown_traffic()
        def send_email_later():
            email_object.send_confirmation_message()

        return HttpResponseRedirect('/accounts/await_confirmation/')

    return render(request, 'signup-phase-one.html', {'form': form})


def create_account(request, email_key):

    email_object = get_object_or_404(Email, most_recent_confirmation_key=email_key)
    email_object.confirm(email_key)

    user_form = UserSignupForm(prefix="user")
    account_form = AccountForm(prefix="account")

    return render(request, 'signup-phase-two.html', {'account_form': account_form,
                                                     'user_form': user_form,
                                                     'email_object': email_object})

