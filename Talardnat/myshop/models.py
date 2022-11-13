from code import interact
from email.policy import default
from unicodedata import category
from django.db import models
from seller.models import seller_detail
from customer.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class shop_detail(models.Model):
    seller_id = models.ForeignKey(seller_detail, on_delete=models.CASCADE, related_name = "shop", null=True)
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=10, null=True)
    in_interact = models.CharField(max_length=100, null=True)
    ex_interact = models.CharField(max_length=64, null=True)
    #expire = models.IntegerField(null=True)
    #queue = models.IntegerField(null=True)
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

    def ordered(self):
        return self.count - 1

class review(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = "rev", null=True)
    shop = models.ForeignKey(shop_detail, on_delete=models.CASCADE, related_name = "rev", null=True)
    score = models.IntegerField(null=True)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"shop: {self.shop} score: {self.score}"

class MyOrder(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True , related_name="order")
    shop = models.ForeignKey(shop_detail, on_delete=models.CASCADE, null=True , related_name="myorder")
    prod = models.ForeignKey(product, on_delete=models.CASCADE, null=True , related_name="ordered")
    count = models.IntegerField(default = 1)

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