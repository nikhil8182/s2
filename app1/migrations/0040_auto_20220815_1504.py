# Generated by Django 3.2.5 on 2022-08-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0039_auto_20220805_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='Table_Down',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sensor',
            name='Table_Pause',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sensor',
            name='Table_Up',
            field=models.BooleanField(default=False),
        ),
    ]