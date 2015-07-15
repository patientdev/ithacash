from django.shortcuts import render
from signup.models import *
from django.core.mail import send_mail

def front(request):
	return render(request, 'front.html')

def apply(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)

		if form.is_valid():
			# Email and kick to /thanks/

			message = ''

			for key, value in request.POST.iteritems():
				key = key.upper()
				message+="%key: %value"

			send_mail('Ithacash Application', message, request.POST['email'], ['shane@patientdev.com'])

	else:
		form = SignUpForm()

	return render(request, 'apply.html', { 'form': form })