from django.shortcuts import render
from .forms import StaffLogin, StaffSignup
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login


def login(request):
    form = StaffLogin(request.POST or None)

    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({'success': True}, status=202, reason="OK: Form values accepted")

            else:
                return JsonResponse({'fail': True}, status=400)
        else:
            return JsonResponse({'fail': True}, status=404, reason="BAD REQUEST: User does not exist")

    else:
        return render(request, 'login.html', {'form': form})


def signup(request):
    form = StaffSignup(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            user = form.save()

            return JsonResponse({'success': True}, status=202, reason="OK: Form values accepted")

        else:
            return JsonResponse(form.errors, status=400)

    return render(request, 'signup.html', {'form': form})
