# Generated by Django 3.2.5 on 2022-01-06 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_alter_sensor_door'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='Door',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='Todays_Bill',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='Total_Bill',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='Units',
        ),
    ]