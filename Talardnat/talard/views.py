from django.shortcuts import render
from django.http import HttpResponse
from myshop.models import shop_detail, product
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'talard/index.html')

def about(request):
    return render(request, 'talard/about.html')

def category(request):
    shop_category = shop_detail.objects.all()
    return render(request, "talard/category.html", {
        "s_category" : shop_category
    })

def allshop(request, category):
    allshop = shop_detail.objects.all()
    return render(request, 'talard/allshop.html', {
        "allshop" : allshop, "category" :category
    })

# def thisshop(request, shop_id):
#     this_shop = shop_detail.objects.get(id=shop_id)
#     #menu = product.objects.filter(shop=this_shop)
#     return render(request, 'talard/shop.html', {
#         "this_shop" : this_shop
#     })


def thisshop(request, shop_id):
    this_shop = shop_detail.objects.get(id=shop_id)
    menu = product.objects.filter(shop=this_shop)
    return render(request, 'talard/shop.html', {
        "this_shop" : this_shop},
        {"menu" : menu
    })