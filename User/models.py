from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField("Телефон", unique=True, max_length=12, blank=True)
    orders_number = models.IntegerField("Количество заказов", default=0)
    orders_sum = models.IntegerField("Сумма заказов", default=0)

    def __str__(self):
        return f'ID: {self.id};\n' \
               f'Имя: {self.username};\n' \
               f'Номер телефона: {self.phone_number};\n' \
               f'Количество заказов: {self.orders_number};\n' \
               f'Сумма заказов: {self.orders_sum}'
