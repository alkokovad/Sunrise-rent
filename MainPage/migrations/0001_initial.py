# Generated by Django 4.0.6 on 2022-07-26 09:24

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название')),
                ('photo', models.ImageField(default='Static/img/about_img.jpg', upload_to='static/img/equipment/', verbose_name='Фото')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('cost_for_half_hour', models.IntegerField(blank=True, default=0, verbose_name='Стоимость 30 минут')),
                ('cost_for_hour', models.IntegerField(blank=True, default=0, verbose_name='Стоимость часа')),
                ('cost_for_3_hours', models.IntegerField(blank=True, default=0, verbose_name='Стоимость 3 часов')),
                ('cost_for_day', models.IntegerField(blank=True, default=0, verbose_name='Стоимость дня')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('status', models.BooleanField(verbose_name='Статус работы')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Время начала аренды')),
                ('rent_time', models.FloatField(verbose_name='Время арнеды')),
                ('cost', models.IntegerField(verbose_name='Стоимость заказа')),
                ('buyer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('equipment_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainPage.equipment')),
            ],
        ),
    ]
