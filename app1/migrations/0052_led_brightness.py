# Generated by Django 4.1.3 on 2022-11-29 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0051_led_b_led_g_led_r'),
    ]

    operations = [
        migrations.AddField(
            model_name='led',
            name='Brightness',
            field=models.IntegerField(default=0),
        ),
    ]
