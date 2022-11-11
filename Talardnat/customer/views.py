from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from customer.models import Profile

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('profile'))
        else:
            return render(request, 'customer/login.html', {
                'message': 'Invalid credentials.'
            })
    return render(request, 'customer/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'customer/login.html', {
        'message': 'You are logged out!'
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.address = form.cleaned_data.get('address')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.state = form.cleaned_data.get('state')
            user.profile.zip = form.cleaned_data.get('zip')
            user.profile.phone = form.cleaned_data.get('phone')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            return HttpResponseRedirect(reverse('customer_login'))
    else:
        form = RegisterForm()
    return render(request,'customer/register.html', {'form': form})

def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('customer_login'))
    return render(request, 'customer/profile.html')