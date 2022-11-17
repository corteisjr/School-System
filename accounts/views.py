from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError


def logout_account(request):
    logout(request)
    return redirect('loginaccount')

def login_account(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {'form':AuthenticationForm})
    else:
        user = authenticate(
            username = request.POST.get('username'),
            password = request.POST.get('password')
        )
        if user is None:
            return render(
                request,
                'registration/login.html',
                {
                    'form': AuthenticationForm(),
                    'error': 'Username and password do not match'
                }
            ) 
        else:
            login(request, user)
            return redirect('home_view')
            