from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import mandrill
import requests
import json
from requests.auth import HTTPBasicAuth
from django.template import Context, loader
from django.conf import settings
from pages.forms import *
from pages.utils import *
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.forms import FlatpageForm


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

    flatpage_form = FlatPageForm(initial={'sites': ('1',)})
    subpage_form = SubPageForm()

    if request.method == 'POST':

        if request.POST.get('form'):

            page_id = request.POST.get('id')

            flatpage = FlatPage.objects.get(id=page_id)
            flatpage_dict = model_to_dict(flatpage)
            subpage = SubPage.objects.get(flatpage=page_id)
            subpage_dict = model_to_dict(subpage)

            return JsonResponse({'flatpage': flatpage_dict, 'subpage': subpage_dict})

        else:

            try:
                flatpage_instance = FlatPage.objects.get(id=request.POST.get('id'))
                subpage_instance = SubPage.objects.get(flatpage=flatpage_instance)
            except (FlatPage.DoesNotExist, SubPage.DoesNotExist, ValueError):
                flatpage_instance = None
                subpage_instance = None

            flatpage_form = FlatPageForm(request.POST, instance=flatpage_instance)
            subpage_form = SubPageForm(request.POST, instance=subpage_instance)

            if flatpage_form.is_valid() and subpage_form.is_valid():

                flatpage = flatpage_form.save(commit=False)
                flatpage.save()
                flatpage_form.save_m2m()

                subpage_form.save(commit=False)
                subpage_form.flatpage = flatpage_form
                subpage_form.save()

            return render(request, 'flatpages/list-pages.html', {'pages': FlatPage.objects.all(), 'flatpage_form': flatpage_form, 'subpage_form': subpage_form})

    else:
        return render(request, 'flatpages/list-pages.html', {'pages': FlatPage.objects.all(), 'flatpage_form': flatpage_form, 'subpage_form': subpage_form})


def template(request):
    return render(request, 'flatpages/template.html')
