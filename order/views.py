from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def show_order(request):
    return HttpResponse("Ok")