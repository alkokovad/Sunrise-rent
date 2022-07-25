from ast import Eq
from django.db import models
from User.models import User

# Create your models here.
class Equipment(models.Model):
    equipment_id = models.AutoField('ID', primary_key=True)
    name = models.TextField('Название', unique=True, blank=True)
    bio = models.TextField('Описание', blank=True)
    cost_for_half_hour = models.IntegerField('Стоимость 30 минут', blank=True)
    cost_for_hour = models.IntegerField('Стоимость часа', blank=True)
    cost_for_3_hours = models.IntegerField('Стоимость 3 часов', blank=True)
    cost_for_4_hours = models.IntegerField('Стоимость 4 часов', blank=True)


    def __str__(self):
        return f'ID: {self.id} Название: {self.name} Описание: {self.bio} Стоимость 30 минут: {self.cost_for_half_hour} Стоимость часа: {self.cost_for_hour} Стоимость 3 часов: {self.cost_for_3_hours} Стоимость 4 часов: {self.cost_for_4_hours}'


class Orders(models.Model):
    id = models.AutoField('ID', primary_key=True)
    buyer_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Время начала аренды')
    rent_time = models.FloatField('Время арнеды')
    cost = models.IntegerField('Стоимость заказа')


    def __str__(self):
        return ''


class History(models.Model):
    id = models.AutoField('ID', primary_key=True)
    buyer_ID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    orders_list = models.TextField('Список входящих заказов', blank=True)
    orders_sum = models.IntegerField('Сумма входящих заказов')


    def __str__(self):
        return ''


class Timing(models.Model):
    date = models.DateField('Дата')
    status = models.BooleanField('Статус работы')
    

    def __str__(self):
        state = 'Не работаем'
        if self.status:
            state = 'Работаем'
        date = str(self.date).split('-')
        date = date[2] + '-' + date[1]
        return f'{date} {state}'


    def date_format(self):
        return str(self.date).split('-')[2]
