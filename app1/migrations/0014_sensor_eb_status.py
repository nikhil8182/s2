# Generated by Django 3.2.5 on 2022-01-05 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_remove_sensor_eb_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='EB_Status',
            field=models.BooleanField(default=False),
        ),
    ]
