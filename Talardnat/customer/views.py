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
        'message': 'You have been logged out!'
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            u = User.objects.get(username=username)
            new = Profile(customer = u)
            new.save()
            return HttpResponseRedirect(reverse('customer_login'))
    else:
        form = RegisterForm()
    return render(request,'customer/register.html', {'form': form})

def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('customer_login'))
    return render(request, 'customer/profile.html')	

# class RegisterView(View):
#     form_1 = RegisterForm
#     template_name = 'customer/register.html'

#     def dispatch(self, request):
#         if request.user.is_authenticated:
#             return redirect(to='homepage')

#     def get(self, request):
#         form = self.form_1(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = self.form_1(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             return redirect(to='customer_login')

#         return render(request, 'customer/register.html', {'form': form})

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect(to='profile')
#     else:
#         profile_form = ProfileForm(instance=request.user.profile)

#     return render(request, 'customer/profile.html', {'profile_form': profile_form})

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             u = User.objects.get(username=username)
#             user = Profile.username
#             new = user(cusname = u)
#             new.save()
#             return HttpResponseRedirect(reverse('customer_login'))
#     else:
#         form = RegisterForm()
#     return render(request,'customer/register.html', {'form': form})

# def profile(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse('customer_login'))
#     return render(request, 'customer/profile.html')

# class ProfileView(View):
#     profile = None

#     def get(self, request):
#         context = {'profile': self.profile, 'segment': 'profile'}
#         return render(request, 'customer/profile.html', context)

#     def post(self, request):
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             profile = form.save()
#             profile.user.firstname = form.cleaned_data.get('firstname')
#             profile.user.lastname = form.cleaned_data.get('lastname')
#             profile.user.save()
#         return redirect('profile')