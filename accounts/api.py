from django.http.response import JsonResponse, HttpResponse
from .models import IthacashAccount
from django.shortcuts import render


def register_account(request):

    user_id = request.POST.get('custom')

    try:
        account = IthacashAccount.objects.get(owner_id=user_id)
        account.registration_complete = True
        account.save()

        # Send welcome email

        # return render(request, 'thanks.html')
        return HttpResponse('Success!')

    except IthacashAccount.DoesNotExist:
        return HttpResponse('Whoops!')
