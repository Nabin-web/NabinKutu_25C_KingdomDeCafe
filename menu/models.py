from django.db import models

# Create your models here


class menu_table(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    desc = models.TextField(max_length=150)
    img = models.FileField()
