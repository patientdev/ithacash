from django.shortcuts import render


def front(request):
    return render(request, 'front.html')


def getting_an_account(request):
    return render(request, 'getting.html')