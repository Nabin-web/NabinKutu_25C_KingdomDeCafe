from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
from .models import menu_table, ordered_item, order_list


@login_required
def showmenu(request):

    if request.method == "POST":
        key = request.POST['key']
        menu_detail = menu_table.objects.filter(Q(name__icontains=key))
        return render(request, "menu.html", {'showmenu': menu_detail},)

    menu_detail = menu_table.objects.all()
    return render(request, "menu.html", {'showmenu': menu_detail}, )



def showorderlist(request):
    current_user = request.user.id
    ordered_food = order_list.objects.all()
    # food_object = order_food_list.objects.get(id=pk)
    # food_object.delete()
    # order = order_food
    # print(order.name)
    # return HttpResponse(order_food.name)
    return render(request, "ordered_list.html", {'order_list': ordered_food, 'current_user':current_user})


def add_order(request, pk):
    user = request.user
    food_id = menu_table.objects.get(id=pk)
    date = datetime.now()
    listt = order_list(user_name=user, food_name=food_id, date=date)
    listt.save()
    return HttpResponse('<script>alert("Added to ordered list")</script>')


def forcancel(request, pk):
    cancel_order = order_list.objects.get(id=pk)
    cancel_order.delete()
    return redirect('/ordered/orderlist')



