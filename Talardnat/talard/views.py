from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import Avg
from myshop.models import shop_detail, product, MyOrder, round
from django.contrib.auth.models import User
from customer.models import Profile as cs
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse, exceptions
from django.db.models import Sum
from .models import *

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
    if not round.objects.filter(round_queue = 0):
        r = None
        allshop = None
    else:
        r = round.objects.get(round_queue = 0)
        allshop = r.shop
    return render(request, 'talard/allshop.html', {
        "allshop" : allshop, "category" :category, "u_id":u_id
    })

def thisshop(request, u_id, shop_id):
    this_shop = shop_detail.objects.get(id=shop_id)
    r = round.objects.all()
    ex = (r.get(shop=this_shop)).expire
    menu = product.objects.filter(shop=this_shop)
    user = User.objects.get(id=u_id)
    customer = cs.objects.get(customer=user)
    reviews = Review.objects.filter(shop=this_shop)

    if request.user.is_authenticated:
        try:
            canReview = MyOrder.objects.filter(customer=request.user.id, shop=this_shop).exists()
        except MyOrder.DoesNotExist:
            canReview = None
    else:
        canReview = None
    
    avg_reviews = reviews.aggregate(avg_rating = Avg('review_rating'))

    return render(request, 'talard/shop.html', {
        "this_shop" : this_shop,
        "menu" : menu, "u_id":u_id,
        "reviews": reviews,
        "canReview": canReview,
        "avg_reviews": avg_reviews,
        "expire":ex,
    })

def buy(request, u_id, shop_id, prod_id):
    shop = shop_detail.objects.get(id=shop_id)
    user = User.objects.get(id=u_id)
    customer = cs.objects.get(customer=user)
    prod = product.objects.get(id=prod_id)
    menu = product.objects.filter(shop=shop)
    oder = MyOrder.objects.filter(shop=shop,customer=customer,prod=prod)
    hadod = oder.exists()
    if not hadod:
        od = MyOrder(shop=shop,customer=customer,prod=prod)
        od.save()
    od = MyOrder.objects.get(shop=shop,customer=customer,prod=prod)
    if request.method == 'POST':
        in_count = request.POST["count"]
        if int(in_count) > 0 and int(in_count) <= prod.prodcount():
            od.count = request.POST["count"]
            od.save()
            prodcount = prod.prodcount() - int(in_count)
            prod.count = prodcount
            prod.save()
            return HttpResponseRedirect(reverse("thisshop", args=(u_id,shop_id)))
            
        return render(request, "talard/shop.html", {"this_shop" : shop,
        "menu" : menu, "u_id":u_id, "message":f"invalid count. Have {prod.prodcount()} got {in_count}"})


def order(request, u_id):
    user = User.objects.get(id=u_id)
    customer = cs.objects.get(customer=user)
    od = MyOrder.objects.filter(customer=customer)
    od2 = MyOrder.objects.filter(customer=customer).values
    return render(request, "talard/order.html", {"order" : od, "u_id":u_id, "od2":od2})

def del_order(request, u_id, oid):
    order = MyOrder.objects.get(id=oid)
    prod = order.prod
    prodcount = prod.prodcount() + order.count
    prod.count = prodcount
    prod.save()
    order.delete()
    return HttpResponseRedirect(reverse("order", args=(u_id,)))
    
def addreview(request, u_id, shop_id):
    url = request.META.get('HTTP_REFERER')
    shop = shop_detail.objects.get(id=shop_id)
    user = cs.objects.get(customer=u_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = Review()
            data.review_text = form.cleaned_data['review_text']
            data.review_rating = form.cleaned_data['review_rating']
            data.shop = shop
            data.user = user
            data.save()
            return redirect(url)


def rating(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('customer_login'))
    if request.method == 'POST':
        form = RateUsForm(request.POST)
        if form.is_valid():
            rate = RateUs()
            rate.rate_text = form.cleaned_data['rate_text']
            rate.rating = form.cleaned_data['rating']
            rate.user = request.user
            rate.save()
            return HttpResponseRedirect(reverse("index"))
    return render(request, 'talard/rate.html')
    

def rateus(request):
    return render(request, 'talard/rate.html')