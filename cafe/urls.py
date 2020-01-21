from django.urls import path
from . import views


urlpatterns = [
    path('', views.show, name='Home-page'),
    path('register/', views.showreg, name='Register-Page'),
    path('home/', views.showhome, name='home-Page'),
    path('food/', views.showfood, name='Food-Page'),
    path('login/', views.showlogin, name='Login-Page'),
    path('menu/', views.showmenu, name='menu-Page'),
    path('chef/', views.showchef, name='chef-Page'),
    path('location/', views.showlocation, name='chef-Page'),
    # path('location/', views.showinfo, name='chef-Page'),
]
