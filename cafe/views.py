from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.


def show(request):
    return render(request, "KingdomDeCafe.html")


def showreg(request):
    return render(request, "Registration.html")


def showhome(request):
    return render(request, "HotelApp.html")


def showfood(request):
    return render(request, "foodgallery.html")


def showlogin(request):
    return render(request, "login.html")


def showmenu(request):
    return render(request, "menu.html")


def showchef(request):
    return render(request, "chef.html")


def showlocation(request):
    return render(request, "location.html")


# def showinfo(request):
#     return render(request, "chef.html")