from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import mandrill, requests, json
from requests.auth import HTTPBasicAuth
from django.template import Context, loader
from django.conf import settings
from .forms import newsletter_subscription_form, send_message_form


@csrf_exempt
def front(request):

    newsletter_form = newsletter_subscription_form(None)
    message_form = send_message_form(None)

    if request.method == 'POST':

        which_form = request.POST.get('form')

        if which_form == 'newsletter_form':

            form = newsletter_subscription_form(request.POST)

            if form.is_valid():
                payload = {
                    'email_address': request.POST.get('subscriber_email_address'),
                    'status': 'subscribed',
                    'merge_fields': {
                        'FNAME': request.POST.get('subscriber_first_name'), 
                        'LNAME': request.POST.get('subscriber_last_name')
                    }
                }

                try:
                    r = requests.post('https://us9.api.mailchimp.com/3.0/lists/933eb82aa4/members/', auth=HTTPBasicAuth('', settings.MAILCHIMP_API_KEY), data=json.dumps(payload))

                    if r.status_code == 200:
                        return JsonResponse({'success': True})

                    else:
                        return JsonResponse({'errors': r}, status=500)

                except requests.exceptions.RequestException as e:
                    return JsonResponse({'errors': str(e)}, status=500)

            else:
                return JsonResponse(form.errors, status=400);

        elif which_form == 'message_form':

            form = message_form(request.POST)

            which = request.POST['which']
            post_data = request.POST.copy()
            del post_data['which']

            subject = 'Message from ithacash.com'

            t = loader.get_template('emails/front.txt')
            c = Context({
                'post_data': post_data
            })
            message = t.render(c)

            mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)

            try:
                mandrill_client.messages.send(
                    {
                        'to': [{'email': 'support@ithacash.com'}],
                        'html': message,
                        'from_name': 'Ithacash.com',
                        'from_email': request.POST['email'],
                        'subject': subject,
                    })

                return (JsonResponse({'success': True}))

            except Exception, e:
                return (JsonResponse({'errors': str(e)}, status=500))

            else:
                return (JsonResponse({'errors': 'else'}, status=500))

    else:
        return render(request, 'front.html', {'newsletter_form': newsletter_form, 'message_form': message_form})


def getting_an_account(request):
    return render(request, 'getting.html')