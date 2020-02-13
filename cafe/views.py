from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from . import models
from .models import Registration_table, Book_table, User_review, user_detail
from django.contrib.auth.models import User


def show(request):
    if request.method == "POST":

        customer_name = request.POST['customername']
        contact_number = request.POST['Contactnumber']
        table_number = request.POST['tablenum']
        number_of_customer = request.POST['customernum']
        arrival_time = request.POST['time']

        User_table_booking = Book_table(Name_of_customer=customer_name, contact_number=contact_number, table_num=table_number,
                                        number_of_customer=number_of_customer, Time=arrival_time )
        User_table_booking.save()
        return HttpResponse('<script>alert("Your Booking is done. Go back <--")</script>')
    return render(request, "KingdomDeCafe.html")


def do_reg(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('Email')
        password = request.POST['password']
        username = request.POST.get('username')
        phone = request.POST.get('phonenumber')
        dob = request.POST.get('dob')
        usr = User(first_name=first_name, last_name=last_name, email=email, username=username)
        usr.set_password(password)
        usr.save()
        new_user = User.objects.get(username=username)
        ud = user_detail(user=new_user, phone=phone, dob=dob)
        ud.save()
    return render(request, "Registration.html")


# def showreg(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('fname')
#         last_name = request.POST.get('lname')
#         email = request.POST.get('Email')
#         password = request.POST.get('password')
#         phone = request.POST.get('phonenumber')
#         dob = request.POST.get('dob')
#         remember = 1
#
#         user = Registration_table(First_name=first_name, Second_name=last_name, Email=email,
#                                                  Password=password, Phone_number=phone, Date_of_birth=dob, Remember_me=remember)
#         user.save()
#         return redirect('/login')
#
#     return render(request, "Registration.html")


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
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("../home")
        else:
            return HttpResponse('wrong username or password')
    # email = request.POST.get('name')
    # print(email)
    # password = request.POST.get('password')
    # print(password)
    # if request.method == 'POST':
    #     usr = Registration_table.objects.get(Email=email, Password=password)
    #     print(usr)
    #     if usr is not None:
    #         return redirect("../", {'logged': usr})
    #     else:
    #         return HttpResponse("wrong password or user does not exist")
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('../home')


def showchef(request):
    return render(request, "chef.html")


def showlocation(request):
    return render(request, "location.html")


def showReview(request):
    user_review_detail = User_review.objects.all()
    if request.method == 'POST':
        username = request.user
        review_desc = request.POST.get('review')

        review = User_review(user=username, review_desc=review_desc)
        review.save()
        return redirect('/review')
    return render(request, "Review.html", {'urd': user_review_detail})


def delete_review(request, pk):
    delete = User_review.objects.get(id=pk)
    delete.delete()
    return redirect('/review')


def update_review(request, pk):
    review = User_review.objects.get(id=pk)
    if request.method == 'POST':
        updated = request.POST.get('review')
        review.review_desc = updated
        review.save()
        return redirect('/review', {'urd': review})

    return render(request, 'update.html', {'review': review})





