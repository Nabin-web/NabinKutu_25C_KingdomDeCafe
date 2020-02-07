from django.urls import path

from . import views

urlpatterns = [
    path('', views.showmenu),
    path('orderlist/', views.showorderlist),
    path('list/<int:pk>', views.add_order),
    path('cancel/<int:pk>/', views.forcancel),


]

