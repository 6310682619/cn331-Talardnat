from django.urls import path, include
from . import views
from talard import views as talard_view

urlpatterns = [
    path('', talard_view.index, name='homepage'),
    path('about', talard_view.about, name='about'),
    path('login', views.login_view, name='customer_login'),
    path('logout', views.logout_view, name='customer_logout'),
    path('signup', views.register, name='register'),
    path('<int:u_id>/profile/', views.profile, name='profile'),
]