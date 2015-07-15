from django.shortcuts import render

def front(request):
	return render(request, 'front.html')

def apply(request):
	return render(request, 'application.html')