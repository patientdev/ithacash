from django.http.response import JsonResponse, HttpResponse
from .models import IthacashAccount
from django.shortcuts import render


def register_account(request):

    user_id = request.POST.get('user_id')

    try:
        account = IthacashAccount.objects.get(owner_id=user_id)
        account.registration_complete = True
        account.save()

        # Send welcome email

        # return render(request, 'thanks.html')
        return HttpResponse('Success!')

    except IthacashUser.DoesNotExist:
        return HttpResponse('Whoops!')
