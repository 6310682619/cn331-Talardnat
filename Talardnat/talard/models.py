from django.db import models
from customer.models import *
from myshop.models import *

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    shop = models.ForeignKey(shop_detail,on_delete=models.CASCADE)
    review_text = models.TextField(max_length=300)
    review_rating = models.IntegerField()

    def __str__(self):
        return f"{self.review_rating}"


class RateUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.rating}"