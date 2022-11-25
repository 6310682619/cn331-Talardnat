from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('talard/<int:u_id>/', views.category, name='talard'),
    path('talard/<str:category>/<int:u_id>/', views.allshop, name='allshop'),
    path('talard/shop/<int:u_id>/<int:shop_id>/', views.thisshop, name='thisshop'),
    path('talard/shop/<int:u_id>/<int:shop_id>/<int:prod_id>/buy/', views.buy, name='buy'),
    path('talard/<int:u_id>/order/', views.order, name='order'),
    path('talard/<int:u_id>/<int:oid>/order/', views.del_order, name='delorder'),
    path('talard/<int:u_id>/<int:oid>/recieved/', views.recieved, name='recieved'),
    path('talard/shop/<int:u_id>/<int:shop_id>/review/', views.addreview, name='addreview'),
    path('rateus/', views.rateus, name='rateus'),
    path('rating/', views.rating, name='rating'),
]