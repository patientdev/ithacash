from django.shortcuts import render
from signup.models import *
from django.core.mail import send_mail
import csv, os
from django.http import HttpResponseRedirect, JsonResponse
from signup.utils import CSVify

def front(request):
	return render(request, 'front.html')

def apply(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)

		if form.is_valid():
			# Append plain text data to CSV then kick to /thanks/

			CSVify(request.POST.copy(), 'signup/data/applications.csv')

			return(HttpResponseRedirect('/thanks'))

		else:
			return (JsonResponse({ 'errors': form.errors.as_json() }))

	else:
		form = SignUpForm()

	return render(request, 'apply.html', { 'form': form.as_p() })