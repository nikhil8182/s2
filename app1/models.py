from django.db import models
from django.db.models.fields import BooleanField
import datetime
# Create your models here.
class Device(models.Model):
    Device_Name = models.CharField(max_length=50,default='')
    Device_Status = models.BooleanField(default=False)
    Device_Type = models.CharField(max_length=50,default='')
    Room = models.CharField(max_length=50,default='')
    Time_Stamp = models.IntegerField(default=0)
    Last_Updated = models.CharField(max_length=70,default='')

    class Meta:
        ordering=['id']

class Sensor(models.Model):
    Voltage = models.IntegerField(default=0)
    Ampere = models.FloatField(default=0.0)
    UPS = models.IntegerField(default=0)
    EB_Status = models.BooleanField(default=False)

    Water_Level = models.IntegerField(default=0)
    Motion_sensor = models.BooleanField(default=False)
    Motion_sensor_2 = models.BooleanField(default=False)    
    Sensor_Time = models.IntegerField(default=0)
    
    Door = models.BooleanField(default=False)
    Door_Motor = models.BooleanField(default=False)    
    Door_Open = models.BooleanField(default=False)
    Door_Close = models.BooleanField(default=False)
    Door_Pause = models.BooleanField(default=False)
    
    Table = models.BooleanField(default=False)
    Table_Up = models.BooleanField(default=False)
    Table_Down = models.BooleanField(default=False)
    Table_Pause = models.BooleanField(default=False)

    Units = models.FloatField(default=0.0)
    #Units = models.FloatField(default=0.0)
    Todays_Bill = models.FloatField(default=0.0)
  #  Todays_Bill = models.FloatField(default=0.0)
    Total_Bill = models.FloatField(default=0.0)
    
    Humidity = models.FloatField(default= 0.0)
    Temperature = models.FloatField(default = 0.0)
    
    
    
    class Meta:
        ordering=['id']
        
class Motion(models.Model):
    Device_Name = models.CharField(max_length=50)
    Device_Status = models.BooleanField(default=False)
    Device_Type = models.CharField(max_length=50,default='')
    Room = models.CharField(max_length=50)
    Time = models.IntegerField(default=0)
    On_State = models.BooleanField(default=False)
    Off_State= models.BooleanField(default=False)
    Time_Stamp = models.IntegerField(default=0)
    Last_Updated = models.CharField(max_length=70,default='')
    
    class Meta:
        ordering=['id']

class Sechdule(models.Model):
    Date = models.CharField(max_length=50)
    Time = models.CharField(max_length=50)
    Device_Name = models.CharField(max_length=50)
    Device_State = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

class Tab(models.Model):
    Tab_Name = models.CharField(max_length=20)
    Tab_Theme = models.CharField(max_length=30)
    Tab_Brightness = models.IntegerField(default=0)
    Tab_Status = models.BooleanField(default=False)
    Tab_Charge = models.IntegerField(default=0)
    Time_Stamp = models.IntegerField(default=0)
    Last_Updated = models.CharField(max_length=70,default='')
    class Meta:
        ordering =['id']

class Table(models.Model):
    Name = models.CharField(max_length=30)
    Height = models.IntegerField(default=0)
    Room = models.CharField(max_length=30)
    Up = models.BooleanField(default=False)
    Down = models.BooleanField(default=False)
    Pause = models.BooleanField(default=False)
    class Meta:
        ordering =['id']

class Fan(models.Model):
    Fan_Name = models.CharField(max_length=30)
    Fan_Status = models.BooleanField(default=False)
    Fan_Speed = models.IntegerField(default=0)
    Device_Type = models.CharField(max_length=50,default='')
    Room = models.CharField(max_length=30)
    Time_Stamp = models.IntegerField(default=0)
    Last_Updated = models.CharField(max_length=70,default='')

    class Meta:
        ordering =['id']
        
class Room(models.Model):
    Room_Name = models.CharField(max_length=30)
    #Fan_Status = models.BooleanField(default=False)
    #Fan_Speed = models.IntegerField(default=0)
    
    class Meta:
        ordering =['id']

class User_Detail(models.Model):
    user_Name = models.CharField(max_length=50)
    user_Room = models.CharField(max_length=50)
    is_Connected_to_Local_Server = models.BooleanField(default=False)

    class Meta:
        ordering =['id']

class Heater(models.Model):
    Heater_Name = models.CharField(max_length=50)
    Heater_Room = models.CharField(max_length=50)
    Heater_Status = models.BooleanField(default=False)
    Device_Type = models.CharField(max_length=50,default='')
    Device_IP = models.CharField(max_length=50)
    Device_MAC = models.CharField(max_length=50)
    Off_Time = models.CharField(max_length=50)
    Ping = models.CharField(max_length=50)
    Time_Stamp = models.IntegerField(default=0)
    Last_Updated = models.CharField(max_length=70,default='')
    
    class Meta:
        ordering =['id']

class Board(models.Model):
    Board_Name = models.CharField(max_length=50)
    Board_Room = models.CharField(max_length=50)
    Device_IP = models.CharField(max_length=50,blank=True)
    Device_MAC = models.CharField(max_length=50,blank=True)    
    Time_Stamp = models.IntegerField(default=0)
    Wifi_Name = models.CharField(max_length=50,blank=True)
    Host_Name = models.CharField(max_length=50,blank=True)
    Announced = models.BooleanField(default=False)
    
    class Meta:
        ordering =['id']

class Onyx(models.Model):
    Command = models.CharField(max_length=50, default='')
    Sender = models.CharField(max_length=50, default='')
    Receiver = models.CharField(max_length=50, default='')
    Reply = models.CharField(max_length=50, default='')
    Time_Stamp = models.IntegerField(default=0)
    
    class Meta:
        ordering =['id']

