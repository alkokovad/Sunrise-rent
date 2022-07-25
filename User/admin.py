from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class MyUserAdmin(UserAdmin):
    list_display = ['username', 'phone_number', 'orders_number', 'orders_sum']


admin.site.register(User, MyUserAdmin)