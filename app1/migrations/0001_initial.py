# Generated by Django 3.2.5 on 2021-12-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Device_Name', models.CharField(default='onwords', max_length=50)),
                ('Device_Status', models.BooleanField(default=False)),
                ('Device_Type', models.CharField(default='smart', max_length=50)),
                ('Room', models.CharField(default='sd', max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fan_Name', models.CharField(max_length=30)),
                ('Fan_Status', models.BooleanField(default=False)),
                ('Fan_Speed', models.IntegerField(default=0)),
                ('Room', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_Name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sechdule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=50)),
                ('Time', models.CharField(max_length=50)),
                ('Device_Name', models.CharField(max_length=50)),
                ('Device_State', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Voltage', models.IntegerField(default=0)),
                ('Ampere', models.FloatField(default=0.0)),
                ('UPS', models.IntegerField(default=0)),
                ('EB_Status', models.BooleanField(default=False)),
                ('Water_Level', models.IntegerField(default=0)),
                ('Motion_sensor', models.BooleanField(default=False)),
                ('Door', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tab_Name', models.CharField(max_length=20)),
                ('Tab_Theme', models.CharField(max_length=30)),
                ('Tab_Brightness', models.IntegerField(default=0)),
                ('Tab_Status', models.BooleanField(default=False)),
                ('Tab_Charge', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_Name', models.CharField(max_length=50)),
                ('user_Room', models.CharField(max_length=50)),
                ('is_Connected_to_Local_Server', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]