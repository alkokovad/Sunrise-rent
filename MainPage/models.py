from django.db import models
from User.models import User


class Equipment(models.Model):
    name = models.CharField('Название', max_length=256, unique=True)
    photo = models.ImageField('Фото', upload_to='Static/img/equipment/', default='Static/img/about_img.jpg')
    description = models.TextField('Описание', blank=True, null=True)
    is_active = models.BooleanField('В работе', default=True)
    cost_for_half_hour = models.IntegerField('Стоимость 30 минут', blank=True, default=0)
    cost_for_hour = models.IntegerField('Стоимость часа', blank=True, default=0)
    cost_for_3_hours = models.IntegerField('Стоимость 3 часов', blank=True, default=0)
    cost_for_day = models.IntegerField('Стоимость дня', blank=True, default=0)

    class Meta:
        verbose_name = 'Инвентарь'
        verbose_name_plural = 'Инвентарь'

    def __str__(self):
        return f'ID: {self.id}\n' \
               f'Название: {self.name}\n' \
               f'Описание: {self.description}\n' \
               f'Стоимость 30 минут: {self.cost_for_half_hour}\n' \
               f'Стоимость часа: {self.cost_for_hour}\n' \
               f'Стоимость 3 часов: {self.cost_for_3_hours}\n' \
               f'Стоимость дня: {self.cost_for_day}'


class Orders(models.Model):
    buyer_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    equipment_id = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField('Время начала аренды')
    rent_time = models.FloatField('Время арнеды')
    cost = models.IntegerField('Стоимость заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'ID: {self.id}\n' \
               f'Инвентарь: {self.equipment_id.name}\n' \
               f'Покупатель: {self.buyer_id.username}\n' \
               f'Начало аренды: {self.start_time}\n' \
               f'Время аренды: {self.rent_time}\n' \
               f'Стоимость: {self.cost}'


class Schedule(models.Model):
    date = models.DateField('Дата')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    def __str__(self):
        state = 'Работаем'
        date = str(self.date).split('-')
        date = date[2] + '-' + date[1]
        return f'{date} {state}'

    def get_day(self):
        return str(self.date).split('-')[2]
