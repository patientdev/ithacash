from django.shortcuts import render
from signup.models import *
from django.core.mail import send_mail
import csv, os, random, string
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView


def front(request):
    return render(request, 'front.html')


def account(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            # Append plain text data to CSV for Cyclos import
            # Then generate a temp pasword for them to replace in Cyclos
            # Then kick to /thanks/

            # We're not showing the tin_last4 field on the application form
            # Let's auto-gen tin_last4 from incoming tin
            obj = form.save(commit=False)
            obj.tin_last4 = request.POST['tin'][-4:]
            obj.save()

            temp_password = ''.join(random.choice(string.ascii_letters) for i in range(12))

            CyclosCSV(request.POST.copy(), 'signup/data/cyclos.csv')
            IthacashCSV(request.POST.copy(), 'signup/data/ithacash.csv')

            return (JsonResponse({'success': 'true'}))

        else:
            return (JsonResponse({'errors': form.errors.as_json()}))

    else:
        form = SignUpForm()
    return render(request, 'account.html', {'form': form})


def getting_an_account(request):
    return render(request, 'getting.html')


def sign_up(request):
    return render(request, 'sign-up.html')


def sign_up_individual(request):
    return render(request, 'sign-up-individual.html')


def apply_individual(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            # Append plain text data to CSV for Cyclos import
            # Then generate a temp pasword for them to replace in Cyclos
            # Then kick to /thanks/

            # We're not showing the tin_last4 field on the application form
            # Let's auto-gen tin_last4 from incoming tin
            obj = form.save(commit=False)
            obj.tin_last4 = request.POST['tin'][-4:]
            obj.save()

            temp_password = ''.join(random.choice(string.ascii_letters) for i in range(12))

            CyclosCSV(request.POST.copy(), 'signup/data/cyclos.csv')
            IthacashCSV(request.POST.copy(), 'signup/data/ithacash.csv')

            return (JsonResponse({'success': 'true'}))

        else:
            return (JsonResponse({'errors': form.errors.as_json()}))

    else:
        form = SignUpForm()
    return render(request, 'apply-individual.html', {'form': form})


def apply_freelancer(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            # Append plain text data to CSV for Cyclos import
            # Then generate a temp pasword for them to replace in Cyclos
            # Then kick to /thanks/

            # We're not showing the tin_last4 field on the application form
            # Let's auto-gen tin_last4 from incoming tin
            obj = form.save(commit=False)
            obj.tin_last4 = request.POST['tin'][-4:]
            obj.save()

            temp_password = ''.join(random.choice(string.ascii_letters) for i in range(12))

            CyclosCSV(request.POST.copy(), 'signup/data/cyclos.csv')
            IthacashCSV(request.POST.copy(), 'signup/data/ithacash.csv')

            return (JsonResponse({'success': 'true'}))

        else:
            return (JsonResponse({'errors': form.errors.as_json()}))

    else:
        form = SignUpForm()
    return render(request, 'apply-freelancer.html', {'form': form})
