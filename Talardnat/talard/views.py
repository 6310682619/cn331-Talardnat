from django.shortcuts import render
from django.http import HttpResponse
from myshop.models import shop_detail

# Create your views here.

def index(request):
    return render(request, 'talard/index.html')

def about(request):
    return render(request, 'talard/about.html')

def category(request):
    shop_category = shop_detail.objects.all()
    
    #food = shop_detail.objects.get(category="food")
    #utensil = shop_detail.objects.get(category="utensil")
    return render(request, "talard/category.html", {"s_category" : shop_category})
    #return render(request, "talard/shop.html", {"food" : food}, {"utensil" : utensil})

def allshop(request, category):
    allshop = shop_detail.objects.all()
    return render(request, 'talard/allshop.html', {"allshop" : allshop, "category" :category} )