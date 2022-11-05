from code import interact
from unicodedata import category
from django.db import models
from seller.models import seller_detail
from customer.models import Profile

# Create your models here.
class shop_detail(models.Model):
    seller_id = models.ForeignKey(seller_detail, on_delete=models.CASCADE, related_name = "shop", null=True)
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=10, null=True)
    in_interact = models.CharField(max_length=100, null=True)
    ex_interact = models.CharField(max_length=64, null=True)
    expire = models.IntegerField(default=0)
    queue = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.id} name: {self.name} queue: {self.queue}"

class product(models.Model):
    shop = models.ForeignKey(shop_detail, on_delete=models.CASCADE, related_name = "prod", null=True)
    product_name = models.CharField(max_length=64)
    price = models.IntegerField(null=True)
    product_im = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.id} product: {self.product_name}"

class review(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = "rev", null=True)
    shop = models.ForeignKey(shop_detail, on_delete=models.CASCADE, related_name = "rev", null=True)
    score = models.IntegerField(null=True)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"shop: {self.shop} score: {self.score}"

