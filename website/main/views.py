from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.contrib import messages




# Create your views here.

def index(request):
    data = {
        'title': "Home Page"
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')


@login_required
def profile_view(request):
    return render(request, 'web/profile.html' )

def register(request):
    return render(request, 'registration/register.html')

# REGISTRATION FORM



