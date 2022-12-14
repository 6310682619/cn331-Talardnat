from django import forms
from .models import *
from django.forms import ChoiceField

class ShopForm(forms.ModelForm):
    cat = [
        ("food", "food"),
        ("utensil", "utensil"),
    ]
    category = ChoiceField(
        choices=cat
    )
  
    class Meta:
        model = shop_detail
        
        fields = ['name', 'category', 'in_interact', 'ex_interact', 'shop_im', 'payment']
  
class ProductForm(forms.ModelForm):
  
    class Meta:
        model = product
        fields = ['product_name', 'price', 'count', 'product_im']

class QueueForm(forms.ModelForm):
    
    class Meta:
        model = round
        fields = ['round_queue']