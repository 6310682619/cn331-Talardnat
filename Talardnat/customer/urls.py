from django.urls import path
from . import views
from talard import views as talard_view

urlpatterns = [
    path('', talard_view.index, name='homepage'),
    path('about', talard_view.about, name='about'),
    path('customer/login', views.login_view, name='login'),
    path('customer/logout', views.logout_view, name='logout'),
    path('customer/register', views.register, name='register'),
    path('customer/<int:u_id>/profile/', views.profile, name='profile'),
]