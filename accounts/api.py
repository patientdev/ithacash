from django.http.response import JsonResponse, HttpResponse, HttpResponseNotFound, HttpResponseServerError
from .models import IthacashAccount
from django.shortcuts import render, redirect
from exceptions import AttributeError


def register_account(request):

    try:
        user_id = request.POST.get('id')
    except AttributeError:
        user_id = request.GET.get('id')

    try:
        account = IthacashAccount.objects.get(owner_id=user_id)
        if not account.registration_complete:
            account.registration_complete = True
            account.save()

            # Send welcome email
            account.send_awaiting_verification_message()

            return redirect('/thanks/')

        else:
            return redirect('/thanks/')

    except IthacashAccount.DoesNotExist as e:
        return HttpResponseNotFound(e)

    except:
        return HttpResponseServerError("Unexpected error: %s" % sys.exc_info()[0])
