# Generated by Django 3.2.8 on 2022-06-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_remove_sensor_motion_sensor_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='Motion_sensor_Time',
            field=models.IntegerField(default=0),
        ),
    ]