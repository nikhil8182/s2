# Generated by Django 4.1.3 on 2022-11-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0050_alter_led_hexa_alter_led_rgb'),
    ]

    operations = [
        migrations.AddField(
            model_name='led',
            name='B',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='led',
            name='G',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='led',
            name='R',
            field=models.IntegerField(default=0),
        ),
    ]
