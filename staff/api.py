from accounts.models import IthacashUser, IthacashAccount
from .models import IthacashStaff
from django.http.response import JsonResponse, HttpResponseRedirect
from django.core import serializers
from itertools import chain
from django.db.models import Q
import json


def get_tin(user_list):
    tins = IthacashAccount.objects.get()


def confirm_staff(request, confirmation_key):

    try:
        staff = IthacashStaff.objects.get(most_recent_confirmation_key=confirmation_key)
        staff.confirm(confirmation_key)

        return HttpResponseRedirect('/staff/login/')

    except IthacashStaff.DoesNotExist:
        return HttpResponse("That user wasn't found", status=404)


def search_users(request):

    if request.method == 'GET':

        q = request.GET['q']

        if q:

            search_results = IthacashUser.objects.select_related().filter(Q(full_name__icontains=q) | Q(username__icontains=q) | Q(emails__address__icontains=q)).values('emails__address', 'username', 'full_name', 'id', 'accounts__account_type', 'accounts__entity_name', 'accounts__is_ssn', 'accounts')

            tins = {}
            for user in search_results:
                try:
                    account = IthacashAccount.objects.get(id=user['accounts'])
                    tins[user['id']] = account.tin
                except:
                    pass

            if search_results.exists():
                return JsonResponse({'results': json.dumps(list(search_results)), 'tins': tins}, safe=False, status=200)

            else:
                return JsonResponse(json.dumps(list({''})), safe=False, status=204)

        else:
            return JsonResponse(json.dumps(list({''})), safe=False, status=204)
