from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:sid>/', views.index, name='myshop_index'),
    path('shop/<int:shop_id>/', views.shop, name='myshop'),
    path('shop/<int:shop_id>/product/', views.product, name='product'),
    path('shop/<int:shop_id>/<int:prod_id>/delprod/', views.del_prod, name='delprod'),
    ]