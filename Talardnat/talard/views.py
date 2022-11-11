from django.shortcuts import render
from django.http import HttpResponse
from myshop.models import shop_detail, product, MyOrder
from django.contrib.auth.models import User
from customer.models import Profile as cs
from .forms import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse, exceptions

# Create your views here.

def index(request):
    return render(request, 'talard/index.html')

def about(request):
    return render(request, 'talard/about.html')

def category(request, u_id):
    shop_category = shop_detail.objects.all()
    return render(request, "talard/category.html", {
        "s_category" : shop_category, "u_id":u_id
    })

def allshop(request, category, u_id):
    allshop = shop_detail.objects.all()
    return render(request, 'talard/allshop.html', {
        "allshop" : allshop, "category" :category, "u_id":u_id
    })

def thisshop(request, u_id, shop_id):
    this_shop = shop_detail.objects.get(id=shop_id)
    menu = product.objects.filter(shop=this_shop)
    return render(request, 'talard/shop.html', {
        "this_shop" : this_shop,
        "menu" : menu, "u_id":u_id
    })

def buy(request, u_id, shop_id, prod_id):
    shop = shop_detail.objects.get(id=shop_id)
    customer = cs.objects.get(customer=u_id)
    prod = product.objects.get(pk=prod_id)
    menu = product.objects.filter(shop=shop)
    oder = MyOrder.objects.filter(shop=shop,customer=customer)
    hadod = oder.exists()
    if not hadod:
        od = MyOrder(shop=shop,customer=customer)
        od.save()
    od = MyOrder.objects.get(shop=shop,customer=customer)
    if request.method == 'POST':
        in_count = request.POST["count"]
        if int(in_count) > 0 and int(in_count) <= prod.prodcount():
            od.prod.add(prod)
            od.count = request.POST["count"]
            od.save()
            prodcount = prod.prodcount() - int(in_count)
            prod.count = prodcount
            prod.save()
            return HttpResponseRedirect(reverse("thisshop", args=(u_id,shop_id)))
            
        return render(request, "talard/shop.html", {"this_shop" : shop,
        "menu" : menu, "u_id":u_id, "message":f"invalid count. Have {prod.prodcount()} got {in_count}"})

    