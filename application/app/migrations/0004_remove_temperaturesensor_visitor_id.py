# Generated by Django 3.2 on 2023-03-30 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_temperaturesensor_visitor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temperaturesensor',
            name='visitor_id',
        ),
    ]
