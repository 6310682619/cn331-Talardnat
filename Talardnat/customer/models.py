from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.

class customer_detail(models.Model):
    cusname = models.ForeignKey(User, on_delete=models.CASCADE, null=True , related_name="cusname")

    def __str__(self):
        return f"{self.cusname}"

