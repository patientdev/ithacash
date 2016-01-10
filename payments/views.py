from django.http.response import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.models import IthacashAccount
from payments.models import SignUpPayment
from payments.utils import PaypalValidator
import requests


@csrf_exempt
def paypal_ipn_endpoint(request):
    is_legit = PaypalValidator().validate_paypal_ipn(request.POST.copy())

    if is_legit:
        pass

    else:
        return HttpResponseBadRequest("This request was not validated by paypal.")

    if request.POST['payment_status'] == "Completed":
        account_id = request.POST['custom'].split('_')[1]
        account = IthacashAccount.objects.get(id=account_id)

        payment = SignUpPayment.objects.create(account=account, amount=request.POST['payment_gross'])

        r = requests.patch('/accounts/api/register_account', {'id': account.id})

    return HttpResponse("PROCESSED.")
