# Generated by Django 3.2.5 on 2022-01-06 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_auto_20220106_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='Door',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sensor',
            name='Todays_Bill',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='sensor',
            name='Total_Bill',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='sensor',
            name='Units',
            field=models.FloatField(default=0.0),
        ),
    ]
