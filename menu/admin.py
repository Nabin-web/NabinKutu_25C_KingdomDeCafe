from django.contrib import admin
#
from .models import menu_table, ordered_item


class menu_table_admin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc', 'img')


class ordered_item_admin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(menu_table, menu_table_admin)

admin.site.register(ordered_item, ordered_item_admin)

