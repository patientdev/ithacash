from django.shortcuts import render
from signup.models import *
from django.core.mail import send_mail
import csv, os

def front(request):
	return render(request, 'front.html')

def apply(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)

		if form.is_valid():
			# Email and kick to /thanks/

			post = request.POST.copy()

			message = ''
			fieldnames = []

			for key, value in post.iteritems():
				fieldnames.append(key)

			csvfile = 'signup/data/applications.csv';

			if not os.path.isfile(csvfile):
				f = open(csvfile, 'a')
				writer = csv.DictWriter(f, fieldnames=fieldnames)

				writer.writeheader()

			else:
				f = open(csvfile, 'a')
				writer = csv.DictWriter(f, fieldnames=fieldnames)

			rows = {}
			rows.update(post.iteritems())

			writer.writerow(rows)

			# print message

		# else:
		# 	print form.error()

		# send_mail('Ithacash Application', message, request.POST['email'], ['shane@patientdev.com'])

	else:
		form = SignUpForm()

	return render(request, 'apply.html', { 'form': form.as_p() })