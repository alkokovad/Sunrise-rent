from ast import Or
from django.contrib import admin
from .models import Equipment, Orders, History, Timing

# Register your models here.
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Timing)
class Timing(admin.ModelAdmin):
    pass