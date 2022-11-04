from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, exceptions
from django.contrib.auth.models import User, Group
from seller.models import seller_detail
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "seller/seller_index.html")


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