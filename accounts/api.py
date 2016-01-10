from django.http.response import JsonResponse, HttpResponse
from .models import IthacashAccount
from django.shortcuts import render


def register_account(request):

    user_id = request.GET.get('id')

    try:
        account = IthacashAccount.objects.get(owner_id=user_id)
        if not account.registration_complete:
            account.registration_complete = True
            account.save()

            # Send welcome email

            # return render(request, 'thanks.html')
            return HttpResponse('Success!')

        else:
            return HttpResponse('Already set!')

    except IthacashAccount.DoesNotExist:
        return HttpResponse('Whoops!')
