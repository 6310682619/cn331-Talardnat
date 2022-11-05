from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True , related_name="customer")

    def __str__(self):
        return f"{self.customer}"

class MyOrder(models.Model):
    c_name = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True , related_name="c_name")
