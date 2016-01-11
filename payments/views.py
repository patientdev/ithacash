from django.http.response import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.models import IthacashAccount
from payments.models import SignUpPayment
from payments.utils import PaypalValidator

from django.shortcuts import redirect


@csrf_exempt
def paypal_ipn_endpoint(request):
    is_legit = PaypalValidator().validate_paypal_ipn(request.POST.copy())

<<<<<<< HEAD
    if is_legit:
        pass

    else:
        return HttpResponseBadRequest("This request was not validated by paypal.")

    if request.POST['payment_status'] == "Completed":
        if 'custom' in request.POST:
            account_id = request.POST['custom'].split('_')[1]
            account = IthacashAccount.objects.get(id=account_id)
=======
    if is_legit and request.POST['payment_status'] == "Completed":
        account_id = request.POST['custom'].split('_')[1]
        account = IthacashAccount.objects.get(id=account_id)
>>>>>>> develop

            payment = SignUpPayment.objects.create(account=account, amount=request.POST['payment_gross'])

<<<<<<< HEAD
            account.send_awaiting_verification_message()
=======
        return redirect('accounts.api.register_account', id=account.id)

    else:
        return HttpResponseBadRequest("This request was not validated by paypal.")
>>>>>>> develop

    return HttpResponse("PROCESSED.")
