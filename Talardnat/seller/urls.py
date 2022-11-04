from django.urls import path, include
from . import views
from talard import views as tview

urlpatterns = [
    path("talard", tview.index, name="taview"),
    path('', views.index, name='seller_index'),
    path('login', views.login_view, name='seller_login'),
    path('logout', views.logout_view, name='seller_logout'),
    path('signup', views.signup, name='seller_signup'),
    ]