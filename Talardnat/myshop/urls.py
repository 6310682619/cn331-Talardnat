from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:sid>/', views.index, name='myshop_index'),
    path('shop/<int:shop_id>/', views.shop, name='myshop'),
    ]