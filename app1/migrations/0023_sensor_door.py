# Generated by Django 3.2.8 on 2022-04-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_remove_sensor_door'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='Door',
            field=models.BooleanField(default=False),
        ),
    ]