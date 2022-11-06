from django import forms
from .models import *
from myshop.models import MyOrder
from django.forms import ChoiceField

class OrderForm(forms.ModelForm):
  
    class Meta:
        model = MyOrder
        fields = ['count']