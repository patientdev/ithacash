from django.shortcuts import render
from .forms import StaffLogin, StaffSignup
from django.http.response import JsonResponse


def login(request):
    form = StaffLogin()
    return render(request, 'login.html', {'form': form})


def signup(request):
    form = StaffSignup(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            user = form.save()

            print user

            return JsonResponse({'success': True}, status=202, reason="OK: Form values accepted")

        else:
            return JsonResponse(form.errors, status=400)

    return render(request, 'signup.html', {'form': form})
