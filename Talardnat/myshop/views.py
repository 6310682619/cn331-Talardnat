from django.shortcuts import render, redirect
from .models import shop_detail
from .models import product as pd
from seller.models import seller_detail
from django.urls import reverse, exceptions
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import ProductForm
# Create your views here.

def index(request, sid):
    shop = shop_detail.objects.filter(seller_id= sid)
    return render(request, "myshop/myshop_index.html", {"shop":shop})

def shop(request, shop_id):
    s = shop_detail.objects.get(pk=shop_id)
    user = User.objects.get(username=s.seller_id)
    seller = seller_detail.objects.get(sname = user)
    return render(request, "myshop/shop.html", {"shop" : s, "seller":seller.id})

def product(request,shop_id):
    s = shop_detail.objects.get(pk=shop_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            newprod = form.save(commit=False)
            newprod.shop = s
            newprod.save()
    else:
        form = ProductForm()
    prod = pd.objects.filter(shop=s)
    return render(request, 'myshop/product.html', {'form' : form, 'product':prod, 'shop_id':shop_id})

def del_prod(request,shop_id,prod_id):
    prod = pd.objects.get(pk = prod_id)
    prod.delete()
    return HttpResponseRedirect(reverse("product", args=(shop_id,)))