from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import mandrill
import requests
import json
import bleach
from requests.auth import HTTPBasicAuth
from django.template import Context, loader
from django.conf import settings
from pages.forms import *
from pages.utils import *
from pages.models import UploadedFiles
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.forms import FlatpageForm
from os.path import basename


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


def page_creator(request):

    flatpage_form = FlatPageForm(initial={'sites': ('1',)})
    subpage_form = SubPageForm()

    if request.method == 'POST':

        if request.POST.get('action') == 'edit':

            page_id = request.POST.get('id')

            flatpage = FlatPage.objects.get(id=page_id)
            flatpage_dict = model_to_dict(flatpage)
            subpage = SubPage.objects.get(flatpage=page_id)
            subpage_dict = model_to_dict(subpage)

            return JsonResponse({'flatpage': flatpage_dict, 'subpage': subpage_dict})

        elif request.POST.get('action') == 'del':

            page_id = request.POST.get('id')

            try:
                flatpage = FlatPage.objects.get(id=page_id)
                subpage = SubPage.objects.get(flatpage=page_id)
            except (FlatPage.DoesNotExist, SubPage.DoesNotExist):
                pass

            flatpage.delete()
            subpage.delete()

            return JsonResponse({'page_id': page_id})

        else:

            try:
                flatpage_instance = FlatPage.objects.get(id=request.POST.get('id'))
                subpage_instance = SubPage.objects.get(flatpage=flatpage_instance)
            except (FlatPage.DoesNotExist, SubPage.DoesNotExist, ValueError):
                flatpage_instance = None
                subpage_instance = None

            flatpage_form = FlatPageForm(request.POST, instance=flatpage_instance)
            subpage_form = SubPageForm(request.POST, instance=subpage_instance)

            print flatpage_form.errors

            if flatpage_form.is_valid() and subpage_form.is_valid():

                # Let's whitelist tags for POSTed content
                flatpage = flatpage_form.save(commit=False)
                bleach.ALLOWED_TAGS.extend(['p', 'mark', 'h3', 'h4', 'br', 'img'])
                bleach.ALLOWED_ATTRIBUTES['a'].extend(['class', 'target'])
                bleach.ALLOWED_ATTRIBUTES['img'] = ['src', 'height', 'width']
                flatpage.content = bleach.clean(flatpage.content, tags=bleach.ALLOWED_TAGS, attributes=bleach.ALLOWED_ATTRIBUTES, strip=True)
                flatpage.save()
                flatpage_form.save_m2m()

                subpage = subpage_form.save(commit=False)
                subpage.flatpage = flatpage
                print subpage.meta_keywords
                print subpage.meta_desc
                subpage.save()

                return render(request, 'flatpages/list-pages.html', {'pages': FlatPage.objects.all(), 'flatpage_form': FlatPageForm(initial={'sites': ('1',)}), 'subpage_form': SubPageForm()})

            else:

                return render(request, 'flatpages/list-pages.html', {'pages': FlatPage.objects.all(), 'flatpage_form': flatpage_form, 'subpage_form': subpage_form})

    else:
        return render(request, 'flatpages/list-pages.html', {'pages': FlatPage.objects.all(), 'flatpage_form': flatpage_form, 'subpage_form': subpage_form})


def template(request):
    return render(request, 'flatpages/template.html')


def files(request):
    files = UploadedFiles.objects.all().order_by('id').reverse()

    upload_form = FileUploadForm(request.POST or None, request.FILES or None)

    if request.method == 'GET' and 'json' in request.GET:
        return render(request, 'files_json.html', {'files': files}, content_type="application/json")

    elif request.method == 'GET' and 'json' not in request.GET:

        return render(request, 'files.html', {'files': files, 'upload_form': upload_form})

    elif request.method == 'POST':

        if upload_form.is_valid():
            uploaded_file = upload_form.save(commit=False)
            uploaded_file.title = basename(uploaded_file.file.path)
            uploaded_file.save()
            return render(request, 'files.html', {'files': files, 'upload_form': upload_form})

        else:
            return render(request, 'files.html', {'files': files, 'upload_form': upload_form})
