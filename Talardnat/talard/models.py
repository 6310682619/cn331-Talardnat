from django.db import models
from customer.models import *
from myshop.models import *
from django.db.models import Avg, Count
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    shop = models.ForeignKey(shop_detail,on_delete=models.CASCADE)
    review_text = models.TextField(max_length=300)
    review_rating = models.IntegerField()

    def averageReview(self):
        reviews = Review.objects.filter(shop=self, status=True).aggregate(average=Avg('review_rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

class RateUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.rating}"