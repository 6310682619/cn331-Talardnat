from code import interact
from unicodedata import category
from django.db import models
from seller.models import seller_detail

# Create your models here.
class shop_detail(models.Model):
    seller_id = models.ForeignKey(seller_detail, on_delete=models.CASCADE, related_name = "shop", null=True)
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64, null=True)
    interact = models.CharField(max_length=200, null=True)
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

