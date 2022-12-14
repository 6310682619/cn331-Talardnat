from code import interact
from email.policy import default
from unicodedata import category
from django.db import models
from seller.models import seller_detail
from customer.models import Profile
from django.utils import timezone

# Create your models here.
class shop_detail(models.Model):
    seller_id = models.ForeignKey(seller_detail, on_delete=models.CASCADE, related_name = "shop", null=True)
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=10, null=True)
    in_interact = models.CharField(max_length=100, null=True)
    ex_interact = models.CharField(max_length=64, null=True)
    shop_im = models.ImageField(upload_to='images/', default = "images/cartoon-style-cafe-front-shop-view_134830-697.webp")
    payment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"({self.id}) {self.name}"

class product(models.Model):
    shop = models.ForeignKey(shop_detail, on_delete=models.CASCADE, related_name = "prod", null=True)
    product_name = models.CharField(max_length=64)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=8)
    product_im = models.ImageField(upload_to='images/')
    count = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.product_name}"

    def prodprice(self):
        return self.price
    
    def prodcount(self):
        return self.count

class MyOrder(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True , related_name="order")
    shop = models.ForeignKey(shop_detail, on_delete=models.CASCADE, null=True , related_name="myorder")
    prod = models.ForeignKey(product, on_delete=models.CASCADE, null=True , related_name="ordered")
    count = models.IntegerField(default = 1)
    confirmpay = models.CharField(default = "not pay yet.", max_length=64)
    confirmrecieved = models.CharField(default = "not recieve yet.", max_length=64)
    date = models.DateTimeField(default=timezone.now, editable=False, blank=True)

    def price(self):
        return self.prod.price * self.count

class round(models.Model):
    shop = models.ManyToManyField(shop_detail, blank=True, related_name = "addqueue")
    round_queue = models.IntegerField(default = 0)
    numshop = models.IntegerField(default = 0)
    expire = models.DateTimeField(null=True)
    start = models.DateTimeField(null=True)

    def __str__(self):
        return f"round: {self.round_queue}"