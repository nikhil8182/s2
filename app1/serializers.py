from rest_framework import serializers
from .models import *


class DeviceSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Device_Name = serializers.CharField(required=False)
    Device_Status = serializers.BooleanField(required=False)
    Device_Type = serializers.CharField(required=False)
    Room = serializers.CharField(required=False)
    Time_Stamp = serializers.IntegerField(required=False)
    Last_Updated = serializers.CharField(required=False)

    def create(self, validated_data):
        return Device.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Device_Name = validated_data.get("Device_Name", instance.Device_Name)
        instance.Device_Status = validated_data.get(
            "Device_Status", instance.Device_Status
        )
        instance.Device_Type = validated_data.get("Device_Type", instance.Device_Type)
        instance.Room = validated_data.get("Room", instance.Room)
        instance.Time_Stamp = validated_data.get("Time_Stamp", instance.Time_Stamp)
        instance.Last_Updated = validated_data.get(
            "Last_Updated", instance.Last_Updated
        )
        # instance.Device_D = validated_data.get('Device_D', instance.Device_D)
        # instance.Device_E = validated_data.get('Device_E', instance.Device_E)

        # instance.Device_I = validated_data.get('Device_I', instance.Device_I)
        # instance.Device_J = validated_data.get('Device_J', instance.Device_J)
        # instance.Device_K = validated_data.get('Device_K', instance.Device_K)
        # instance.Device_L = validated_data.get('Device_L', instance.Device_L)
        # instance.Device_M = validated_data.get('Device_M', instance.Device_M)
        instance.save()
        return instance

    class Meta:
        model = Device
        fields = ["__all__"]


class SensorSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Voltage = serializers.IntegerField(required=False)
    Ampere = serializers.FloatField(required=False)
    UPS = serializers.IntegerField(required=False)
    EB_Status = serializers.BooleanField(required=False)

    Water_Level = serializers.IntegerField(required=False)
    Motion_sensor = serializers.BooleanField(required=False)
    Motion_sensor_2 = serializers.BooleanField(required=False)
    Sensor_Time = serializers.IntegerField(required=False)
    Door = serializers.BooleanField(required=False)

    Door_Motor = serializers.BooleanField(required=False)
    Door_Open = serializers.BooleanField(required=False)
    Door_Close = serializers.BooleanField(required=False)
    Door_Pause = serializers.BooleanField(required=False)

    Table = serializers.BooleanField(required=False)
    Table_Up = serializers.BooleanField(required=False)
    Table_Down = serializers.BooleanField(required=False)
    Table_Pause = serializers.BooleanField(required=False)

    Units = serializers.FloatField(required=False)
    Todays_Bill = serializers.FloatField(required=False)
    #  Todays_Bill = serializers.FloatField(required=False)
    Total_Bill = serializers.FloatField(required=False)

    Humidity = serializers.FloatField(required=False)
    Temperature = serializers.FloatField(required=False)

    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Voltage = validated_data.get("Voltage", instance.Voltage)
        instance.Ampere = validated_data.get("Ampere", instance.Ampere)
        instance.UPS = validated_data.get("UPS", instance.UPS)
        instance.EB_Status = validated_data.get("EB_Status", instance.EB_Status)

        instance.Water_Level = validated_data.get("Water_Level", instance.Water_Level)
        instance.Motion_sensor = validated_data.get(
            "Motion_sensor", instance.Motion_sensor
        )
        instance.Motion_sensor_2 = validated_data.get(
            "Motion_sensor_2", instance.Motion_sensor_2
        )
        instance.Sensor_Time = validated_data.get("Sensor_Time", instance.Sensor_Time)
        instance.Door = validated_data.get("Door", instance.Door)

        instance.Door_Motor = validated_data.get("Door_Motor", instance.Door_Motor)
        instance.Door_Open = validated_data.get("Door_Open", instance.Door_Open)
        instance.Door_Close = validated_data.get("Door_Close", instance.Door_Close)
        instance.Door_Pause = validated_data.get("Door_Pause", instance.Door_Pause)

        instance.Table = validated_data.get("Table", instance.Table)
        instance.Table_Up = validated_data.get("Table_Up", instance.Table_Up)
        instance.Table_Down = validated_data.get("Table_Down", instance.Table_Down)
        instance.Table_Pause = validated_data.get("Table_Pause", instance.Table_Pause)

        instance.Units = validated_data.get("Units", instance.Units)
        instance.Todays_Bill = validated_data.get("Todays_Bill", instance.Todays_Bill)
        # instance.Todays_Bill = validated_data.get('Todays_Bill', instance.Todays_Bill)
        instance.Total_Bill = validated_data.get("Total_Bill", instance.Total_Bill)

        instance.Humidity = validated_data.get("Humidity", instance.Humidity)
        instance.Temperature = validated_data.get("Temperature", instance.Temperature)

        instance.save()
        return instance

    class Meta:
        model = Sensor
        fields = ["__all__"]


class MotionSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Device_Name = serializers.CharField(required=False)
    Device_Status = serializers.BooleanField(required=False)
    Device_Type = serializers.CharField(required=False)
    Room = serializers.CharField(required=False)
    Time = serializers.IntegerField(required=False)
    On_State = serializers.BooleanField(required=False)
    Off_State = serializers.BooleanField(required=False)
    Time_Stamp = serializers.IntegerField(required=False)
    Last_Updated = serializers.CharField(required=False)

    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Device_Name = validated_data.get("Device_Name", instance.Device_Name)
        instance.Device_Status = validated_data.get(
            "Device_Status", instance.Device_Status
        )
        instance.Device_Type = validated_data.get("Device_Type", instance.Device_Type)
        instance.Room = validated_data.get("Room", instance.Room)
        instance.Time = validated_data.get("Time", instance.Time)
        instance.On_State = validated_data.get("On_State", instance.On_State)
        instance.Off_State = validated_data.get("Off_State", instance.Off_State)
        instance.Time_Stamp = validated_data.get("Time_Stamp", instance.Time_Stamp)
        instance.Last_Updated = validated_data.get(
            "Last_Updated", instance.Last_Updated
        )

        instance.save()
        return instance

    class Meta:
        model = Motion
        fields = ["__all__"]


class Serial(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Time = serializers.CharField(required=False, allow_blank=True, max_length=100)
    Date = serializers.CharField(required=False, allow_blank=True, max_length=100)
    Device_Name = serializers.CharField(
        required=False, allow_blank=True, max_length=100
    )
    Device_State = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Sechdule.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.title = validated_data.get('title', instance.title)
        instance.Time = validated_data.get("Time", instance.Time)
        instance.Date = validated_data.get("Date", instance.Date)
        instance.Device_Name = validated_data.get("Device_Name", instance.Device_Name)
        instance.Device_State = validated_data.get(
            "Device_State", instance.Device_State
        )
        instance.save()
        return instance

    class Meta:
        model = Sechdule
        fields = ["id", "Time", "Date", "Device_Name", "Device_State"]


class TabSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Tab_Name = serializers.CharField(required=False, allow_blank=True, max_length=20)
    Tab_Theme = serializers.CharField(required=False, allow_blank=True, max_length=20)
    Tab_Brightness = serializers.IntegerField(required=False)
    Tab_Status = serializers.BooleanField(required=False)
    Tab_Charge = serializers.IntegerField(required=False)
    Time_Stamp = serializers.IntegerField(required=False)
    Last_Updated = serializers.CharField(required=False)

    def create(self, validated_data):
        return Tab.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.title = validated_data.get('title', instance.title)
        instance.Tab_Name = validated_data.get("Tab_Name", instance.Tab_Name)
        instance.Tab_Charge = validated_data.get("Tab_Charge", instance.Tab_Charge)
        instance.Tab_Brightness = validated_data.get(
            "Tab_Brightness", instance.Tab_Brightness
        )
        instance.Tab_Status = validated_data.get("Tab_Status", instance.Tab_Status)
        instance.Time_Stamp = validated_data.get("Time_Stamp", instance.Time_Stamp)
        instance.Last_Updated = validated_data.get(
            "Last_Updated", instance.Last_Updated
        )
        instance.save()
        return instance

    class Meta:
        model = Tab
        fields = ["__all__"]


class TableSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Name = serializers.CharField(required=False, allow_blank=True, max_length=20)
    Height = serializers.IntegerField(required=False)
    Room = serializers.CharField(required=False)
    Up = serializers.BooleanField(required=False)
    Down = serializers.BooleanField(required=False)
    Pause = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Tab.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.title = validated_data.get('title', instance.title)
        instance.Name = validated_data.get("Name", instance.Name)
        instance.Height = validated_data.get("Height", instance.Height)
        instance.Room = validated_data.get("Room", instance.Room)
        instance.Up = validated_data.get("Up", instance.Up)
        instance.Down = validated_data.get("Down", instance.Down)
        instance.Pause = validated_data.get("Pause", instance.Pause)

        instance.save()
        return instance

    class Meta:
        model = Table
        fields = ["__all__"]


class FanSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Fan_Name = serializers.CharField(required=False, allow_blank=True, max_length=20)
    Fan_Status = serializers.BooleanField(required=False)
    Fan_Speed = serializers.IntegerField(required=False)
    Device_Type = serializers.CharField(required=False)
    Room = serializers.CharField(required=False, max_length=30)
    Time_Stamp = serializers.IntegerField(required=False)
    Last_Updated = serializers.CharField(required=False)

    def create(self, validated_data):
        return Fan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.title = validated_data.get('title', instance.title)
        instance.Fan_Name = validated_data.get("Fan_Name", instance.Fan_Name)
        instance.Fan_Status = validated_data.get("Fan_Status", instance.Fan_Status)
        instance.Fan_Speed = validated_data.get("Fan_Speed", instance.Fan_Speed)
        instance.Device_Type = validated_data.get("Device_Type", instance.Device_Type)
        instance.Room = validated_data.get("Room", instance.Room)
        instance.Time_Stamp = validated_data.get("Time_Stamp", instance.Time_Stamp)
        instance.Last_Updated = validated_data.get(
            "Last_Updated", instance.Last_Updated
        )
        # instance.Tab_Brightness = validated_data.get('Tab_Brightness', instance.Tab_Brightness)
        instance.save()
        return instance

    class Meta:
        model = Fan
        fields = ["__all__"]


class RoomSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Room_Name = serializers.CharField(required=False, allow_blank=True, max_length=20)
    # Fan_Status      = serializers.BooleanField(required=False)
    # Fan_Speed  = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.title = validated_data.get('title', instance.title)
        instance.Room_Name = validated_data.get("Room_Name", instance.Room_Name)
        # instance.Fan_Status  = validated_data.get('Fan_Status', instance.Fan_Status )
        # instance.Fan_Speed   = validated_data.get('Fan_Speed', instance.Fan_Speed)
        # instance.Tab_Brightness = validated_data.get('Tab_Brightness', instance.Tab_Brightness)
        instance.save()
        return instance

    class Meta:
        model = Room
        fields = ["__all__"]


class UserSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_Name = serializers.CharField(required=False, allow_blank=True, max_length=20)
    user_Room = serializers.CharField(required=False, allow_blank=True, max_length=20)
    is_Connected_to_Local_Server = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return User_Detail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.title = validated_data.get('title', instance.title)
        instance.user_Name = validated_data.get("user_Name", instance.user_Name)
        instance.user_Room = validated_data.get("user_Room", instance.user_Room)
        instance.is_Connected_to_Local_Server = validated_data.get(
            "is_Connected_to_Local_Server", instance.is_Connected_to_Local_Server
        )
        # instance.Tab_Brightness = validated_data.get('Tab_Brightness', instance.Tab_Brightness)
        instance.save()
        return instance

    class Meta:
        model = User_Detail
        fields = ["__all__"]


class HeaterSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Heater_Name = serializers.CharField(required=False)
    Heater_Room = serializers.CharField(required=False)
    Heater_Status = serializers.BooleanField(required=False)
    Device_Type = serializers.CharField(required=False)
    Device_IP = serializers.CharField(required=False)
    Device_MAC = serializers.CharField(required=False)
    Off_Time = serializers.CharField(required=False)
    Ping = serializers.CharField(required=False)
    Time_Stamp = serializers.IntegerField(required=False)
    Last_Updated = serializers.CharField(required=False)

    def create(self, validated_data):
        return Heater.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Heater_Name = validated_data.get("Heater_Name", instance.Heater_Name)
        instance.Heater_Room = validated_data.get("Heater_Room", instance.Heater_Room)
        instance.Heater_Status = validated_data.get(
            "Heater_Status", instance.Heater_Status
        )
        instance.Device_Type = validated_data.get("Device_Type", instance.Device_Type)
        instance.Device_IP = validated_data.get("Device_IP", instance.Device_IP)
        instance.Device_MAC = validated_data.get("Device_MAC", instance.Device_MAC)
        instance.Off_Time = validated_data.get("Off_Time", instance.Off_Time)
        instance.Ping = validated_data.get("Ping", instance.Ping)
        instance.Time_Stamp = validated_data.get("Time_Stamp", instance.Time_Stamp)
        instance.Last_Updated = validated_data.get(
            "Last_Updated", instance.Last_Updated
        )

        instance.save()
        return instance

    class Meta:
        model = Heater
        fields = ["__all__"]


class BoardSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Board_Name = serializers.CharField(required=False)
    Board_Room = serializers.CharField(required=False)
    Device_IP = serializers.CharField(required=False)
    Device_MAC = serializers.CharField(required=False)
    Time_Stamp = serializers.IntegerField(required=False)
    Wifi_Name = serializers.CharField(required=False)
    Host_Name = serializers.CharField(required=False)
    Announced = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Board.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Board_Name = validated_data.get("Board_Name", instance.Board_Name)
        instance.Board_Room = validated_data.get("Board_Room", instance.Board_Room)
        instance.Device_IP = validated_data.get("Device_IP", instance.Device_IP)
        instance.Device_MAC = validated_data.get("Device_MAC", instance.Device_MAC)
        instance.Time_Stamp = validated_data.get("Time_Stamp", instance.Time_Stamp)
        instance.Wifi_Name = validated_data.get("Wifi_Name", instance.Wifi_Name)
        instance.Host_Name = validated_data.get("Host_Name", instance.Host_Name)
        instance.Announced = validated_data.get("Announced", instance.Announced)

        instance.save()
        return instance

    class Meta:
        model = Board
        fields = ["__all__"]


class OnyxSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Command = serializers.CharField(required=False)
    Sender = serializers.CharField(required=False)
    Receiver = serializers.CharField(required=False)
    Reply = serializers.CharField(required=False)
    Time_Stamp = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Onyx.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Command = validated_data.get("Command", instance.Command)
        instance.Sender = validated_data.get("Sender", instance.Sender)
        instance.Receiver = validated_data.get("Receiver", instance.Receiver)
        instance.Reply = validated_data.get("Reply", instance.Reply)
        instance.Time_Stamp = validated_data.get("Time_Stamp", instance.Time_Stamp)

        instance.save()
        return instance

    class Meta:
        model = Onyx
        fields = ["__all__"]


class emSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    voltage = serializers.IntegerField(required=False)
    ampere = serializers.FloatField(required=False)
    ups = serializers.IntegerField(required=False)
    eb_status = serializers.BooleanField(required=False)
    units = serializers.FloatField(required=False)
    announced = serializers.BooleanField(required=False)
    announcement_time = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return em.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.voltage = validated_data.get("voltage", instance.voltage)
        instance.ampere = validated_data.get("ampere", instance.ampere)
        instance.ups = validated_data.get("ups", instance.ups)
        instance.eb_status = validated_data.get("eb_status", instance.eb_status)
        instance.units = validated_data.get("units", instance.units)
        instance.announced = validated_data.get("announced", instance.announced)
        instance.announcement_time = validated_data.get(
            "announcement_time", instance.announcement_time
        )

        instance.save()
        return instance

    class Meta:
        model = em
        fields = ["__all__"]


class waterSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    level = serializers.IntegerField(required=False)
    time_stamp = serializers.IntegerField(required=False)
    motor_status = serializers.BooleanField(required=False)
    announced = serializers.BooleanField(required=False)
    announcement_time = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return water.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.level = validated_data.get("level", instance.level)
        instance.time_stamp = validated_data.get("time_stamp", instance.time_stamp)
        instance.motor_status = validated_data.get(
            "motor_status", instance.motor_status
        )
        instance.announced = validated_data.get("announced", instance.announced)
        instance.announcement_time = validated_data.get(
            "announcement_time", instance.announcement_time
        )

        instance.save()
        return instance

    class Meta:
        model = water
        fields = ["__all__"]
