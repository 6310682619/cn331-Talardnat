from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, exceptions
from django.contrib.auth.models import User, Group
from seller.models import seller_detail
from seller.forms import sellerForm
# Create your views here.

def index(request, sid):
    user = User.objects.get(username=request.user.username)
    isseller = seller_detail.objects.filter(sname=user).exists()
    if not (request.user.is_authenticated and isseller):
        return HttpResponseRedirect(reverse("seller_login"))
    seller = seller_detail.objects.get(sname=user)
    return render(request, "seller/seller_index.html", {'sid': seller.id})

def signup(request):
    if request.method == 'POST':
        form = sellerForm(request.POST)
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
        form = sellerForm()
    return render(request, 'seller/seller_signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        isseller = seller_detail.objects.filter(sname=user).exists()
        if (user is not None) and (isseller):
            login(request, user)
            u = User.objects.get(username=username)
            sell = seller_detail.objects.get(sname=u)
            return HttpResponseRedirect(reverse("seller_index", args=(sell.id,)))
        else:
            return render(request, "seller/seller_login.html", {"message":"Invalid credentials."})
    return render(request, "seller/seller_login.html")

def logout_view(request):
    logout(request)
    return render(request, "seller/seller_login.html", {"message":"You are logged out"})
