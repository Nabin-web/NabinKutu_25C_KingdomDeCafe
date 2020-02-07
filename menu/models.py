from django.db import models
from django.conf import settings

# Create your models here


class menu_table(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    desc = models.TextField(max_length=150)
    img = models.FileField()


class ordered_item(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)


class order_list(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food_name = models.ForeignKey(menu_table, on_delete=models.CASCADE)
    date = models.DateField()
