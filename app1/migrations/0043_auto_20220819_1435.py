# Generated by Django 3.2.8 on 2022-08-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0042_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='Device_IP',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='board',
            name='Device_MAC',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='board',
            name='Ping',
            field=models.CharField(default='', max_length=50),
        ),
    ]