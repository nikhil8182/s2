# Generated by Django 3.2.8 on 2022-06-18 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_sensor_door_pause'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='Motion_sensor_2',
            field=models.BooleanField(default=False),
        ),
    ]
