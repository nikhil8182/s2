# Generated by Django 3.2.5 on 2022-01-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20220104_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='x',
            field=models.FloatField(default=0.0),
        ),
    ]