from django.db import models

# Create your models here.

class review(models.Model):
    review = models.TextField(max_length=150)

    def __str__(self):
        return f"{self.id} name: {self.review}"