from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import Avg
from myshop.models import shop_detail, product, MyOrder
from django.contrib.auth.models import User
from customer.models import Profile as cs
from .forms import OrderForm, ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse, exceptions
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
    allshop = shop_detail.objects.all()
    return render(request, 'talard/allshop.html', {
        "allshop" : allshop, "category" :category, "u_id":u_id
    })

def thisshop(request, u_id, shop_id):
    this_shop = shop_detail.objects.get(id=shop_id)
    menu = product.objects.filter(shop=this_shop)
    reviews = Review.objects.filter(shop=this_shop)
    # user = cs.objects.get(customer=u_id)

    # if request.method == 'POST':
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         data = Review()
    #         data.review_text = form.cleaned_data['review_text']
    #         data.review_rating = form.cleaned_data['review_rating']
    #         data.shop = this_shop
    #         data.user = user
    #         data.save()

    if request.user.is_authenticated:
        try:
            canReview = MyOrder.objects.filter(customer=request.user.id, shop=this_shop).exists()
        except MyOrder.DoesNotExist:
            canReview = None
    else:
        canReview = None
    
    #avg_reviews = Review.objects.filter(shop=this_shop).aggregate(avg_rating = Avg('review_rating'))

    return render(request, 'talard/shop.html', {
        "this_shop" : this_shop,
        "menu" : menu, "u_id":u_id,
        "reviews": reviews,
        "canReview": canReview,
        # "avg_reviews": avg_reviews,
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


        #reviews = Review.objects.filter(user=user, shop=shop)
        # form = ReviewForm(request.POST)
        # if form.is_valid():
        #     form.save()
        # return redirect(url)

            # form = ReviewForm(request.POST)
            # if form.is_valid():
            #     data = Review()
            #     data.review_text = form.cleaned_data['review_text']
            #     data.review_rating = form.cleaned_data['review_rating']
            #     data.shop = shop
            #     data.user = user
            #     data.save()
            #     return redirect(url)

def rate(request,u_id):
    #rate = RateUs.objects.get(user=u_id)
    pass


# def addreview(request, u_id, shop_id):
# 	shop = shop_detail.objects.get(id=shop_id)
# 	user = cs.objects.get(customer=u_id)
# 	review = Review.objects.create(
# 		user = user,
# 		shop = shop,
# 		review_text = request.POST.get('review_text',False),
# 		review_rating = request.POST.get('review_rating',False),
# 		)

# 	data = {
# 		'user': request.user.username,
# 		'review_text': request.POST.get('review_text',False),
# 		'review_rating': request.POST.get('review_rating',False),
# 	}
# 	avg_reviews = Review.objects.filter(shop=shop).aggregate(avg_rating = Avg('review_rating'))

# 	return JsonResponse({'bool':True, 'data': data, 'avg_reviews': avg_reviews})