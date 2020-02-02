from django.contrib import admin
#
from . models import menu_table


class menu_table_admin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc', 'img')


admin.site.register(menu_table, menu_table_admin)

