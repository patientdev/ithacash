from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import mandrill
import requests
import json
from requests.auth import HTTPBasicAuth
from django.template import Context, loader
from django.conf import settings
from .forms import newsletter_subscription_form, send_message_form
from pages.forms import PageCreatorForm


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
                    'status': 'subscribed'
                }

                try:
                    r = requests.post('https://us9.api.mailchimp.com/3.0/lists/ec92ed377f/members/', auth=HTTPBasicAuth('', settings.MAILCHIMP_API_KEY), json=payload)

                    if r.status_code == 200:
                        return JsonResponse({'success': True}, status=200)

                    elif r.status_code == 400:
                        return JsonResponse({'errors': 'already exists'}, status=400)

                    else:
                        return JsonResponse({'errors': r.json()}, status=500)

                except requests.exceptions.RequestException as e:
                    return JsonResponse({'errors': str(e)}, status=500)

            else:
                return JsonResponse({'errors': form.errors}, status=400)

        elif which_form == 'message_form':

            form = send_message_form(request.POST)

            if form.is_valid():

                mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)

                try:
                    result = mandrill_client.messages.send(
                        {
                            'to': [{'email': 'support@ithacash.com'}],
                            'text': request.POST.get('message'),
                            'from_name': 'Ithacash.com',
                            'from_email': request.POST.get('message_from'),
                            'subject': 'Message from ithacash.com',
                        })

                    return (JsonResponse({'success': result}))

                except Exception, e:
                    return (JsonResponse({'errors': str(e)}, status=500))

            else:
                return (JsonResponse({'errors': form.errors}, status=400))

    else:
        return render(request, 'front.html', {'newsletter_form': newsletter_form, 'message_form': message_form})


def getting_an_account(request):
    return render(request, 'getting.html')


def everyone(request):
    return render(request, 'everyone.html')


def style_guide(request):
    return render(request, 'style-guide.html')


@csrf_exempt
def page_creator(request):

    if request.method == 'POST':

        form = PageCreatorForm(request.POST)

        if form.is_valid():

            new_page = form.save(commit=False)

            content = request.POST.get('content')

            new_page_content = ''

            for line in content.splitlines():
                if line:
                    if '<h3>' not in line:
                        line = '<p>%s</p>' % line

                    new_page_content += '%s\n\n' % line

            new_page.content = new_page_content

            form.save()

            return render(request, 'page-creator.html', {'form': PageCreatorForm()})

        else:
            return JsonResponse(form.errors, status=400)

    else:
        form = PageCreatorForm()

    return render(request, 'page-creator.html', {'form': form})

def template(request):
    return render(request, 'flatpages/template.html')
