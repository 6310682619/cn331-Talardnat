from django.urls import path, include
from . import views
from myshop import views as shop
from talard import views as tview

urlpatterns = [
    path("talard", tview.index, name="taview"),
    path('<int:sid>', views.index, name='seller_index'),
    path('login', views.login_view, name='seller_login'),
    path('logout', views.logout_view, name='seller_logout'),
    path('signup', views.signup, name='seller_signup'),
    path('myshop/<int:sid>', shop.index, name="myshop_index"),
    ]