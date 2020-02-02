from datetime import date
from django.db import models
from django.utils.timezone import now
# Create your models here.


class Book_table(models.Model):
    Name_of_customer = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=50)
    table_num = models.CharField(max_length=50)
    number_of_customer = models.IntegerField(default="0")
    Time = models.CharField(default="", max_length=50)
    Date = models.DateField()


class Registration_table(models.Model):
    First_name = models.CharField(max_length=50)
    Second_name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=20)
    Date_of_birth = models.DateField()
    Remember_me = models.BooleanField()


class User_review(models.Model):
    user = models.ForeignKey(Registration_table, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now, editable=False)
    review_desc = models.TextField(max_length=500)


# def __str__(self):
#     return self.name



# class menu_table(models.Model):
#     name = models.CharField(max_length=50)
#     price = models.CharField(max_length=10)
#     desc = models.TextField(max_length=150)
#     img = models.FileField()


