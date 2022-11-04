from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('talard/', views.index, name='talard'),
    path('talard/shop', views.index, name='allshop'),
    path('talard/shop/<int:shop_id>/', views.index, name='shop'),
]