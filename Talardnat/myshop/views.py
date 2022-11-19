from django.shortcuts import render, redirect
from .models import shop_detail,round
from .models import product as pd
from .models import MyOrder as od
from seller.models import seller_detail
from talard.models import Review
from django.urls import reverse, exceptions
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import ProductForm, ShopForm
# Create your views here.

def index(request, sid):
    shop = shop_detail.objects.filter(seller_id= sid)
    seller = seller_detail.objects.get(pk = sid)
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            newshop = form.save(commit=False)
            newshop.seller_id = seller
            newshop.save()
    else:
        form = ShopForm()
    return render(request, "myshop/myshop_index.html", {'form' : form, "shop":shop,"sid":sid})

def shop(request, shop_id):
    s = shop_detail.objects.get(pk=shop_id)
    user = User.objects.get(username=s.seller_id)
    seller = seller_detail.objects.get(sname = user)
    order = od.objects.filter(shop = s)
    queue = s.addqueue.filter()
    if not queue.exists():
        queue = 'none'
    else:
        queue = (s.addqueue.get()).round_queue
    
    return render(request, "myshop/shop.html", {"shop" : s, "seller":seller.id, "order":order, "queue":queue,})

def del_shop(request, shop_id):
    s = shop_detail.objects.get(pk = shop_id)
    user = User.objects.get(username=s.seller_id)
    seller = seller_detail.objects.get(sname = user)
    sid = seller.id
    s.delete()
    return HttpResponseRedirect(reverse("myshop_index", args=(sid,)))

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

def edit(request,shop_id):
    s = shop_detail.objects.get(pk=shop_id)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("myshop", args=(shop_id,)))
    else:
        form = ShopForm(instance=s)
    return render(request, 'myshop/edit.html', {'form' : form, 'shop_id':shop_id})

def editProd(request,shop_id,prod_id):
    p = pd.objects.get(pk=prod_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("product", args=(shop_id,)))
    else:
        form = ProductForm(instance=p)
    return render(request, 'myshop/editprod.html', {'form' : form, 'prod_id':prod_id})

def myreview(request, shop_id):
    s = shop_detail.objects.get(pk=shop_id)
    rev = Review.objects.filter(shop = s)
    return render(request, "myshop/myreview.html", {"rev":rev,"shop_id": shop_id})

def addqueue(request, shop_id, q_id):
    s = shop_detail.objects.get(pk=shop_id)
    allr = round.objects.filter().order_by('round_queue')
    find = allr.filter(shop = s).exists()
    if not find:
        a = round.objects.get(pk = q_id)
        if a.numshop < 9:
            a.shop.add(s)
            a.numshop += 1
            a.save()
        return HttpResponseRedirect(reverse("queue", args=(shop_id,)))
    
    return render(request, "myshop/queue.html", {
            "shop":  s, 
            "round": allr,
            "message":"Already in queue.",
        })

def delqueue(request, shop_id):
    s = shop_detail.objects.get(pk=shop_id)
    allr = round.objects.filter()
    q = allr.filter(shop = s)
    find = q.exists()
    if find:
        q = allr.get(shop = s)
        q.shop.remove(s)
        q.numshop -= 1
        q.save()
    
    return HttpResponseRedirect(reverse("queue", args=(s.id,)))

def queue(request, shop_id):
    s = shop_detail.objects.get(pk=shop_id)
    allr = round.objects.filter().order_by('round_queue')
    found = round.objects.all().exists()
    if not found:
        new_r= round(round_queue = 0)
        new_r.save()
    return render(request, "myshop/queue.html", {
            "shop":  s, 
            "round": allr,
        })
