import requests
from django.conf import settings
from .forms import add_to_mailing_list_form
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse


@csrf_exempt
def add_to_mailing_list(request):

    form = add_to_mailing_list_form(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        mailing_list_id = request.POST.get('mailing_list_id')
        email_address = request.POST.get('email_address')

        mailchimp_endpoint = 'https://us9.api.mailchimp.com/3.0/lists/{}/members/'.format(mailing_list_id)

        payload = {
            'email_address': email_address,
            'status': 'subscribed'
        }

        try:
            r = requests.post(mailchimp_endpoint, auth=requests.auth.HTTPBasicAuth('', settings.MAILCHIMP_API_KEY), json=payload)

            print r.status_code
            
            if r.status_code == 200:
                return JsonResponse({'success': 'true'}, status=200)

            elif r.status_code == 400:
                return JsonResponse({'email_address': ['Email is already signed up']}, status=400)

            else:
                return JsonResponse({'email_address': ['There was an error on our part. We have been automatically notified.']}, status=500)

        except requests.exceptions.RequestException as e:
            return JsonResponse({'errors': str(e)}, status=500)

    else:
        return JsonResponse(form.errors, status=400)
