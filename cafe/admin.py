from django.contrib import admin

# Register your models here.

from .models import Book_table, Registration_table, User_review


class Book_Table_Admin(admin.ModelAdmin):
    list_display = ('Name_of_customer', 'number_of_customer', 'contact_number', 'table_num', 'Date', 'Time')


class Registration_table_admin(admin.ModelAdmin):
    list_display = ('First_name', 'Second_name', 'Email', 'Password', 'Phone_number',  'Date_of_birth', 'Remember_me')


class User_review_table(admin.ModelAdmin):
    list_display = ('user', 'review_desc', 'created_date')


admin.site.register(Book_table, Book_Table_Admin)

admin.site.register(Registration_table, Registration_table_admin)

admin.site.register(User_review, User_review_table)


