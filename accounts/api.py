from django.http.response import JsonResponse, HttpResponse
from .models import IthacashAccount
from django.shortcuts import render


def register_account(request):

    user_id = request.POST.get('id')

    try:
        account = IthacashAccount.objects.get(owner_id=user_id)
        if not account.registration_complete:
            account.registration_complete = True
            account.save()

            # Send welcome email
            account.send_awaiting_verification_message()

            return redirect('/thanks/')

        else:
            return HttpResponse('Already set!')

    except IthacashAccount.DoesNotExist as e:
        return redirect('/whoops/', {'error': e})
