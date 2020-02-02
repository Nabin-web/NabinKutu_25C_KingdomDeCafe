from django.urls import path

from . import views

urlpatterns = [
    path('', views.showmenu),
    path('list/<int:pk>', views.showorderlist)
]

