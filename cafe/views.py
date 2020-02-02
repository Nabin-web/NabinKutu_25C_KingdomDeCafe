from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from . import models
from .models import Registration_table, Book_table, User_review
from django.contrib.auth.models import User


def show(request):
    return render(request, "KingdomDeCafe.html")


def showreg(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('Email')
        password = request.POST.get('password')
        phone = request.POST.get('phonenumber')
        dob = request.POST.get('dob')
        remember = 1

        user = Registration_table(First_name=first_name, Second_name=last_name, Email=email,
                                                 Password=password, Phone_number=phone, Date_of_birth=dob, Remember_me=remember)
        user.save()
        return redirect('/login')

    return render(request, "Registration.html")


def showhome(request):
    if request.method == "POST":
        customer = request.POST.get('customername')
        contact = request.POST.get('Contactnumber')
        table = request.POST.get('tablenum')
        numberofcus = request.POST.get('customernum')
        time = request.POST.get('time')
        date = request.POST.get('date')

        booking_user = Book_table(Name_of_customer=customer, contact_number=contact,
                                  table_num=table, number_of_customer=numberofcus, Time=time, Date=date)
        booking_user.save()
        return redirect('/menu')
    return render(request, "HotelApp.html")


def showfood(request):
    return render(request, "foodgallery.html")


def showlogin(request):
    email = request.POST.get('name')
    print(email)
    password = request.POST.get('password')
    print(password)
    if request.method == 'POST':
        usr = Registration_table.objects.get(Email=email, Password=password)
        print(usr)
        if usr is not None:
            return redirect("../", {'logged': usr})
        else:
            return HttpResponse("wrong password or user does not exist")

    return render(request, "login.html")


def logout(request):
    usr = ''
    return redirect('../', {'logged': usr})


def showchef(request):
    return render(request, "chef.html")


def showlocation(request):
    return render(request, "location.html")


def showReview(request):
    user_review_detail = User_review.objects.all()
    if request.method == 'POST':
        username = Registration_table(request.user.id)
        review = request.POST.get('review')

        rev = User_review(user=username, review_desc=review)
        rev.save()
        return redirect('/review')
    return render(request, "Review.html", {'urd': user_review_detail})

