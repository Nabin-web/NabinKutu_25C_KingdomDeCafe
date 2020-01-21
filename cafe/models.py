from django.db import models

# Create your models here.


class Book_table(models.Model):
    Name_of_customer = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    table_num = models.CharField(max_length=50)
    number_of_customer = models.IntegerField(default="0")
    Date = models.DateField()



