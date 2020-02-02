from django.db import models

from Website.cafe.models import Registration_table
from Website.menu.models import menu_table


class User_order(models.Model):
    Username = models.ForeignKey(Registration_table, on_delete=models.CASCADE)
    Food = models.ForeignKey(menu_table, on_delete=models.CASCADE)
    Date = models.DateField()
