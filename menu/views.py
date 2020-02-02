from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import menu_table


@login_required
def showmenu(request):
    menu_detail = menu_table.objects.all()
    return render(request, "menu.html", {'menu_d': menu_detail})


@login_required
def showorderlist(request, pk):
    order_food = menu_table.objects.get(id=pk)
    return render(request, "ordered_list.html", {'order': order_food})


