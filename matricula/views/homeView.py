from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

@login_required
def home_view(request):
    return render(request, template_name='home/index.html', status=200) 