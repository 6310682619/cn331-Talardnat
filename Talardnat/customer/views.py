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
        u = User.objects.get(username=username)
        iscustomer = Profile.objects.filter(customer=user).exists()
        if (user is not None) and iscustomer:
            login(request, user)
            return HttpResponseRedirect(reverse('profile', args=(u.id,)))
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
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            u = User.objects.get(username=username)
            customer = Profile(customer=u)
            customer.address = form.cleaned_data.get('address')
            customer.city = form.cleaned_data.get('city')
            customer.state = form.cleaned_data.get('state')
            customer.zip = form.cleaned_data.get('zip')
            customer.phone = form.cleaned_data.get('phone')
            customer.save()
            return HttpResponseRedirect(reverse('customer_login'))
    else:
        form = RegisterForm()
    return render(request,'customer/register.html', {'form': form,})

def profile(request,u_id):
    user = User.objects.get(username=request.user.username)
    customer = Profile.objects.filter(customer=user)
    c = Profile.objects.get(customer=user)
    if not (request.user.is_authenticated and customer):
        return HttpResponseRedirect(reverse('customer_login'))
    return render(request, 'customer/profile.html', {'customer':c})