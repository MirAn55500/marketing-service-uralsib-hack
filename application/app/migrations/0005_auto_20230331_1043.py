# Generated by Django 3.2 on 2023-03-31 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_temperaturesensor_visitor_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relaycondition',
            options={'verbose_name': 'Состояние реле', 'verbose_name_plural': 'Состояния реле'},
        ),
        migrations.AlterModelOptions(
            name='temperaturehistory',
            options={'verbose_name': 'Данные с датчиков', 'verbose_name_plural': 'Данные с датчиков'},
        ),
        migrations.AlterModelOptions(
            name='temperaturesensor',
            options={'verbose_name': 'Датчик температуры', 'verbose_name_plural': 'Датчики температуры'},
        ),
    ]
