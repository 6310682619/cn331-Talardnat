from django import forms
from .models import *
from myshop.models import MyOrder
from django.forms import ChoiceField

class OrderForm(forms.ModelForm):
  
    class Meta:
        model = MyOrder
        fields = ['count']

class ReviewForm(forms.ModelForm):
	class Meta:
		model= Review
		fields= ["review_text", "review_rating"]

# class RateUsForm(forms.ModelForm):
# 	class Meta:
# 		model= RateUs
# 		fields= ["rating"]