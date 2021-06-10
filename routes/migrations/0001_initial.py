# Generated by Django 3.2.3 on 2021-06-05 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0003_alter_city_name'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Номер поезда')),
                ('travel_times', models.PositiveSmallIntegerField(verbose_name='Общее время в пути')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_from_city_set', to='cities.city', verbose_name='Из какого города')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_to_city_set', to='cities.city', verbose_name='В какого города')),
                ('trains', models.ManyToManyField(to='trains.Train', verbose_name='Список поездов')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
                'ordering': ['travel_times'],
            },
        ),
    ]
