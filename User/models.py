from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    buyer_ID = models.AutoField("ID", primary_key=True)
    username = models.CharField("Имя", unique=True, max_length=50, blank=True)
    phone_number = models.CharField("Телефон", unique=True, max_length=12, blank=True)
    orders_number = models.IntegerField("Количество заказов", default=0)
    orders_sum = models.IntegerField("Сумма заказов", default=0)


    def __str__(self):
        return f'ID: {self.id};\nИмя: {self.name};\nНомер телефона: {self.phone_number};\nКоличество заказов: {self.orders_number};\nСумма заказов: {self.orders_sum}'
