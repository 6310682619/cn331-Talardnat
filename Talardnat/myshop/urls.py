from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:sid>/', views.index, name='myshop_index'),
    path('shop/<int:shop_id>/', views.shop, name='myshop'),
    path('shop/<int:shop_id>/delshop', views.del_shop, name='delshop'),
    path('shop/<int:shop_id>/product/', views.product, name='product'),
    path('shop/<int:shop_id>/<int:prod_id>/delprod/', views.del_prod, name='delprod'),
    path('shop/<int:shop_id>/edit/', views.edit, name='edit'),
    path('shop/<int:shop_id>/myreview/', views.myreview, name='myreview'),
    path('shop/<int:shop_id>/<int:prod_id>/editprod/', views.editProd, name='editprod'),
    path('shop/<int:shop_id>/<int:q_id>/queue/add', views.addqueue, name='addqueue'),
    path('shop/<int:shop_id>/queue/del', views.delqueue, name='delqueue'),
    path('shop/<int:shop_id>/queue/', views.queue, name='queue'),
    ]