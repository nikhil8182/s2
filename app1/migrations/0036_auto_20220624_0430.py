# Generated by Django 3.2.8 on 2022-06-24 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0035_auto_20220621_0820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motion',
            old_name='Device_State',
            new_name='Device_Status',
        ),
        migrations.RenameField(
            model_name='motion',
            old_name='Device_Room',
            new_name='Room',
        ),
    ]