from django.shortcuts import render

from .models import shop_detail
from seller.models import seller_detail
from django.urls import reverse, exceptions
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.

def index(request, sid):
    shop = shop_detail.objects.filter(seller_id= sid)
    return render(request, "myshop/myshop_index.html", {"shop":shop})

def shop(request, shop_id):
    s = shop_detail.objects.get(pk=shop_id)
    user = User.objects.get(username=s.seller_id)
    seller = seller_detail.objects.get(sname = user)
    return render(request, "myshop/shop.html", {"shop" : s, "seller":seller.id})