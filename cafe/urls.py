from django.urls import path, include


from . import views


urlpatterns = [
    path('', views.show, name='Home-page'),
    path('register/', views.showreg, name='Register-Page'),
    path('home/', views.showhome, name='home-Page'),
    path('food/', views.showfood, name='Food-Page'),
    path('login/', views.showlogin, name='Login-Page'),
    path('menu/', include('menu.urls'), name='menu-Page'),
    path('ordered/', include('menu.urls'), name='menu-Page'),
    path('chef/', views.showchef, name='chef-Page'),
    path('location/', views.showlocation, name='chef-Page'),
    path('review/', views.showReview, name='chef-Page'),
    path('logout/', views.logout, name='logout')

]
