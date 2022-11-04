from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, exceptions
from django.contrib.auth.models import User, Group
from seller.models import seller_detail
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "seller/seller_index.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            u = User.objects.get(username=username)
            new = seller_detail(sname = u)
            new.save()
            return HttpResponseRedirect(reverse("seller_login"))
    else:
        form = UserCreationForm()
    return render(request, 'seller/seller_signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        isseller = seller_detail.objects.filter(sname=user).exists()
        if (user is not None) and (isseller):
            login(request, user)
            return HttpResponseRedirect(reverse("seller_index"))
        else:
            return render(request, "seller/seller_login.html", {"message":"Invalid credentials."})
    return render(request, "seller/seller_login.html")

def logout_view(request):
    logout(request)
    return render(request, "seller/seller_login.html", {"message":"You are logged out"})