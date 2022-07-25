# Generated by Django 4.0.6 on 2022-07-21 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, unique=True, verbose_name='Название')),
                ('bio', models.TextField(blank=True, verbose_name='Описание')),
                ('cost_for_half_hour', models.IntegerField(blank=True, verbose_name='Стоимость 30 минут')),
                ('cost_for_hour', models.IntegerField(blank=True, verbose_name='Стоимость часа')),
                ('cost_for_3_hours', models.IntegerField(blank=True, verbose_name='Стоимость 3 часов')),
                ('cost_for_4_hours', models.IntegerField(blank=True, verbose_name='Стоимость 4 часов')),
            ],
        ),
        migrations.CreateModel(
            name='Timing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('status', models.BooleanField(verbose_name='Статус работы')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Время начала аренды')),
                ('rent_time', models.FloatField(verbose_name='Время арнеды')),
                ('cost', models.IntegerField(verbose_name='Стоимость заказа')),
                ('buyer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('equipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainPage.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('orders_list', models.TextField(blank=True, verbose_name='Список входящих заказов')),
                ('orders_sum', models.IntegerField(verbose_name='Сумма входящих заказов')),
                ('buyer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainPage.orders')),
            ],
        ),
    ]