from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import mandrill
import requests
import json
import bleach
import staff.settings as staff_settings
from requests.auth import HTTPBasicAuth
from django.template import Context, loader
from django.conf import settings
from pages.forms import *
from pages.utils import PageCreatorBleaching
from pages.models import UploadedFiles
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.forms import FlatpageForm
from os.path import basename


@csrf_exempt
def front(request):

    return render(request, 'front.html')


def getting_an_account(request):
    return render(request, 'getting.html')


def everyone(request):
    return render(request, 'everyone.html')


def style_guide(request):
    return render(request, 'style-guide.html')


def page_creator(request):

    if request.user.is_authenticated():

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

                if flatpage_form.is_valid() and subpage_form.is_valid():

                    # Let's whitelist tags for POSTed content
                    flatpage = flatpage_form.save(commit=False)

                    # Sanitize incoming content using bleach
                    flatpage.content = PageCreatorBleaching(flatpage.content)

                    flatpage.save()
                    flatpage_form.save_m2m()

                    subpage = subpage_form.save(commit=False)
                    subpage.flatpage = flatpage
                    subpage.save()

                    return render(request, 'pages/page-creator.html', {'pages': FlatPage.objects.all(), 'flatpage_form': FlatPageForm(initial={'sites': ('1',)}), 'subpage_form': SubPageForm()})

                else:

                    return render(request, 'pages/page-creator.html', {'pages': FlatPage.objects.all(), 'flatpage_form': flatpage_form, 'subpage_form': subpage_form})

        else:
            return render(request, 'pages/page-creator.html', {'pages': FlatPage.objects.all(), 'flatpage_form': flatpage_form, 'subpage_form': subpage_form})

    else:
        return redirect('/staff/login/')


def template(request):
    return render(request, 'flatpages/template.html')


def files(request):

    if request.user.is_authenticated():

        files = UploadedFiles.objects.all().order_by('id').reverse()

        upload_form = FileUploadForm(request.POST or None, request.FILES or None)

        if request.method == 'GET' and 'json' in request.GET:
            return render(request, 'pages/files_json.json', {'files': files}, content_type="application/json")

        elif request.method == 'GET' and 'json' not in request.GET:

            return render(request, 'pages/files.html', {'files': files, 'upload_form': upload_form})

        elif request.method == 'POST':

            if upload_form.is_valid():
                uploaded_file = upload_form.save(commit=False)
                uploaded_file.title = basename(uploaded_file.file.path)
                uploaded_file.save()
                return render(request, 'pages/files.html', {'files': files, 'upload_form': upload_form})

            else:
                return render(request, 'pages/files.html', {'files': files, 'upload_form': upload_form})

    else:
        return redirect('/staff/login/')
