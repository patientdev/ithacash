from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from hendrix.experience import crosstown_traffic
from accounts.models import Email
from signup.models import SignUpForm
from django import forms

@require_http_methods(["POST"])
def confirm_email_address(request):
    try:
        email = Email.objects.get(address=request.POST['email_address'])
    except Email.DoesNotExist:
        return HttpResponseNotFound()  # TODO: Make this more coherent.

    key = request.POST['key']

    success = email.confirm(key)

    if success:
        pass
        # redirect to a good place
    else:
        # Tell them they failed.
        pass


class EmailForm(forms.ModelForm):

    class Meta:
        fields = ['address']
        model = Email


def signup_phase_one(request):
    form = EmailForm(request.POST)

    if form.is_valid():
        email_object = form.save()

        @crosstown_traffic()
        def send_email_later():
            email_object.send_confirmation_message()

        return HttpResponseRedirect('/accounts/await_confirmation/')

    return render(request, 'signup-email.html', {'form': form})



