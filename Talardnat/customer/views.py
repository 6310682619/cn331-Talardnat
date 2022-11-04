from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from customer.models import customer_profile

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        iscustomer = customer_profile.objects.filter(cusname=user).exists()

        if (user is not None) and (iscustomer):
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
        'message': 'You have been logged out!'
    })

def user(request):
    return render(request, 'customer/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            u = User.objects.get(username=username)
            new = customer_profile(cusname = u)
            new.save()
            return HttpResponseRedirect(reverse('customer_login'))
    else:
        form = RegisterForm()
    return render(request,'customer/register.html', {'form': form})

def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('customer_login'))
    return render(request, 'customer/profile.html')		