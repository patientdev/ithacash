from django.shortcuts import render
from signup.models import *
from django.core.mail import send_mail
import csv, os, random, string
from django.http import HttpResponseRedirect, JsonResponse
from signup.utils import CyclosCSV, IthacashCSV

def front(request):
	return render(request, 'front.html')

def apply(request):
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

			temp_password = ''.join(str(v) for v in random.sample(range(0, 9), 5))

			CyclosCSV(request.POST.copy(), 'signup/data/cyclos.csv')
			IthacashCSV(request.POST.copy(), 'signup/data/ithacash.csv')

			return (JsonResponse({ 'success': 'true' }))

		else:
			return (JsonResponse({ 'errors': form.errors.as_json() }))

	else:
		form = SignUpForm()

	return render(request, 'apply.html', { 'form': form.as_p() })
