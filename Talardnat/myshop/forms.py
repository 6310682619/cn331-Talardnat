from django import forms
from .models import *
  
class ProductForm(forms.ModelForm):
  
    class Meta:
        model = product
        fields = ['product_name', 'price', 'product_im']