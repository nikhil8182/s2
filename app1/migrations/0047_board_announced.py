# Generated by Django 4.1.2 on 2022-11-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0046_rename_ping_board_host_name_board_wifi_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='Announced',
            field=models.BooleanField(default=False),
        ),
    ]