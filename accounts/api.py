from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseServerError
from .models import IthacashAccount, Email
from django.shortcuts import render, redirect
from exceptions import AttributeError


def register_account(request):

    try:
        user_id = request.POST.get('id')
    except AttributeError:
        user_id = request.GET.get('id')

    try:
        account = IthacashAccount.objects.get(owner_id=user_id)

        redirect_url = '/thanks/' if account.account_type == 'Individual' else '/thank-you/'

        account.registration_complete = True
        account.save()

        # Send welcome email
        account.send_awaiting_verification_message()

        return redirect(redirect_url)

    except IthacashAccount.DoesNotExist as e:
        return HttpResponseNotFound(e)

    except:
        return HttpResponseServerError("Unexpected error: %s" % sys.exc_info()[0])


def confirm_email(request, email_key):

    if request.method == 'GET':

        try:
            email_object = Email.objects.get(most_recent_confirmation_key=email_key)

            email_object.confirm(email_key)

            return HttpResponseRedirect('/accounts/create_account/{}'.format(email_key))

        except Email.DoesNotExist:
            return HttpResponseServerError('This email was not recognized')

        except Exception, e:
            print e
            return HttpResponseServerError("There was an error and it's our fault, not yours. We've been notified.")

    else:
        return HttpResponseRedirect('/accounts/signup/')
