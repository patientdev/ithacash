from accounts.models import IthacashUser, IthacashAccount
from django.http.response import JsonResponse
from django.core import serializers
from itertools import chain
from django.db.models import Q
import json


def get_tin(user_list):
    tins = IthacashAccount.objects.get()


def search_users(request):

    if request.method == 'GET':

        q = request.GET['q']

        if q:

            search_results = IthacashUser.objects.select_related().filter(Q(full_name__contains=q) | Q(username__contains=q) | Q(emails__address__contains=q)).values('emails__address', 'username', 'full_name', 'id', 'accounts__account_type', 'accounts__entity_name', 'accounts__is_ssn', 'accounts')

            tins = {}
            for user in search_results:
                try:
                    account = IthacashAccount.objects.get(id=user['accounts'])
                    tins[user['id']] = account.tin
                except:
                    pass

            print tins

            if search_results.exists():
                return JsonResponse({'results': json.dumps(list(search_results)), 'tins': tins}, safe=False, status=200)

            else:
                print search_results
                return JsonResponse(json.dumps(list({''})), safe=False, status=204)

        else:
            return JsonResponse(json.dumps(list({''})), safe=False, status=204)
