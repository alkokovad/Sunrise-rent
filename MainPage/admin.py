from django.contrib import admin
from .models import Equipment, Orders, Schedule


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class Schedule(admin.ModelAdmin):
    pass
