from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
# Create your views here.

from .models import *
from .serializers import *

import pyrebase
import datetime

config = {
    "apiKey": "AIzaSyC-UHZlYoFZX_otZDBOxlskclyebZFAtdc",
    "authDomain": "server-check-1c979.firebaseapp.com",
    "databaseURL": "https://server-check-1c979-default-rtdb.firebaseio.com",
    "storageBucket": "server-check-1c979.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

state = True

class Device_details(APIView):
    def get(self, request, format=None):
        snippets = Device.objects.all()
        serializer = DeviceSerializers(snippets, many=True)
        return Response(serializer.data)
    
    #def post(self, request, format=None):
     #   serializer = DeviceSerializers(data=request.data)
      #  if serializer.is_valid():
       #     serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
       # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Device_Change(APIView):
    def get_object(self, pk):
        try:
            return Device.objects.get(pk=pk)
        except Device.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DeviceSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DeviceSerializers(snippet, data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def delete(self, request, pk, format=None):
     #   snippet = self.get_object(pk)
     #   snippet.delete()
     #   return Response(status=status.HTTP_204_NO_CONTENT)



class Sensor_details(APIView):
    def get(self, request, format=None):
        snippets = Sensor.objects.all()
        serializer = SensorSerializers(snippets, many=True)
        return Response(serializer.data)
    
  #  def post(self, request, format=None):
   #     serializer = SensorSerializers(data=request.data)
    #    if serializer.is_valid():
     #       serializer.save()
      #      return Response(serializer.data, status=status.HTTP_201_CREATED)
       # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Sensor_Change(APIView):
    def get_object(self, pk):
        try:
            return Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SensorSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SensorSerializers(snippet, data=request.data)
        if serializer.is_valid():   
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def delete(self, request, pk, format=None):
     #   snippet = self.get_object(pk)
      #  snippet.delete()
       # return Response(status=status.HTTP_204_NO_CONTENT)
       
class Motion_details(APIView):
    def get(self, request, format=None):
        snippets = Motion.objects.all()
        serializer = MotionSerializers(snippets, many=True)
        return Response(serializer.data)
    
  #  def post(self, request, format=None):
   #     serializer = SensorSerializers(data=request.data)
    #    if serializer.is_valid():
     #       serializer.save()
      #      return Response(serializer.data, status=status.HTTP_201_CREATED)
       # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Motion_Change(APIView):
    def get_object(self, pk):
        try:
            return Motion.objects.get(pk=pk)
        except Motion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MotionSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MotionSerializers(snippet, data=request.data)
        if serializer.is_valid():   
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def delete(self, request, pk, format=None):
     #   snippet = self.get_object(pk)
      #  snippet.delete()
       # return Response(status=status.HTTP_204_NO_CONTENT)

class Reminder(APIView):
    def get(self, request, format=None):
        snippets = Sechdule.objects.all()
        serializer = Serial(snippets, many=True)
        return Response(serializer.data)
   
 #   def post(self, request, format=None):
  #      serializer = Serial(data=request.data)
   #     if serializer.is_valid():
    #        serializer.save()
     #       return Response(serializer.data, status=status.HTTP_201_CREATED)
      #  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Reminder_change(APIView):
    def get_object(self, pk):
        try:
            return Sechdule.objects.get(pk=pk)
        except Sechdule.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Serial(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Serial(snippet, data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    def delete(self, request, pk, format=None):
 #       snippet = self.get_object(pk)
  #      snippet.delete()
   #     return Response(status=status.HTTP_204_NO_CONTENT)

class Tab_view(APIView):
    def get(self, request, format=None):
        snippets = Tab.objects.all()
        serializer = TabSerializers(snippets, many=True)
        return Response(serializer.data)
   
#    def post(self, request, format=None):
 #       serializer = TabSerializers(data=request.data)
  #      if serializer.is_valid():
   #         serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
     #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Tab_change(APIView):
    def get_object(self, pk):
        try:
            return Tab.objects.get(pk=pk)
        except Tab.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TabSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TabSerializers(snippet, data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 #   def delete(self, request, pk, format=None):
  #      snippet = self.get_object(pk)
   #     snippet.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)

class Table_view(APIView):
    def get(self, request, format=None):
        snippets = Table.objects.all()
        serializer = TableSerializers(snippets, many=True)
        return Response(serializer.data)
   
#    def post(self, request, format=None):
 #       serializer = TableSerializers(data=request.data)
  #      if serializer.is_valid():
   #         serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
     #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Table_change(APIView):
    def get_object(self, pk):
        try:
            return Table.objects.get(pk=pk)
        except Table.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TableSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TableSerializers(snippet, data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 #   def delete(self, request, pk, format=None):
  #      snippet = self.get_object(pk)
   #     snippet.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)




class Fan_view(APIView):
    def get(self, request, format=None):
        snippets = Fan.objects.all()
        serializer = FanSerializers(snippets, many=True)
        return Response(serializer.data)
   
 #   def post(self, request, format=None):
  #      serializer = FanSerializers(data=request.data)
   #     if serializer.is_valid():
    #        serializer.save()
     #       return Response(serializer.data, status=status.HTTP_201_CREATED)
      #  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Fan_change(APIView):
    def get_object(self, pk):
        try:
            return Fan.objects.get(pk=pk)
        except Fan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FanSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FanSerializers(snippet, data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 #   def delete(self, request, pk, format=None):
  #      snippet = self.get_object(pk)
   #     snippet.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)

class Room_view(APIView):
    def get(self, request, format=None):
        snippets = Room.objects.all()
        serializer = RoomSerializers(snippets, many=True)
        return Response(serializer.data)   

 #   def post(self, request, format=None):
 #       serializer = RoomSerializers(data=request.data)
  #      if serializer.is_valid():
   #         serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
     #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Room_change(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RoomSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RoomSerializers(snippet, data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def delete(self, request, pk, format=None):
      #  snippet = self.get_object(pk)
      #  snippet.delete()
      #  return Response(status=status.HTTP_204_NO_CONTENT)

class User_view(APIView):
    def get(self, request, format=None):
        snippets = User_Detail.objects.all()
        serializer = UserSerializers(snippets, many=True)
        return Response(serializer.data)
#    def post(self, request, format=None):
 #       serializer = UserSerializers(data=request.data)
#        if serializer.is_valid():
 #           serializer.save()
  #          return Response(serializer.data, status=status.HTTP_201_CREATED)
   #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class User_change(APIView):
    def get_object(self, pk):
        try:
            return User_Detail.objects.get(pk=pk)
        except User_Detail.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializers(snippet, data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   # def delete(self, request, pk, format=None):
     #   snippet = self.get_object(pk)
     #   snippet.delete()
     #   return Response(status=status.HTTP_204_NO_CONTENT)

class Heater_view(APIView):
    def get(self, request, format=None):
        snippets = Heater.objects.all()
        serializer = HeaterSerializers(snippets, many=True)
        return Response(serializer.data)
#    def post(self, request, format=None):
 #       serializer = HeaterSerializers(data=request.data)
#        if serializer.is_valid():
 #           serializer.save()
  #          return Response(serializer.data, status=status.HTTP_201_CREATED)
   #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Heater_change(APIView):
    def get_object(self, pk):
        try:
            return Heater.objects.get(pk=pk)
        except Heater.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = HeaterSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = HeaterSerializers(snippet, data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   # def delete(self, request, pk, format=None):
     #   snippet = self.get_object(pk)
     #   snippet.delete()
     #   return Response(status=status.HTTP_204_NO_CONTENT)


class Board_view(APIView):
    def get(self, request, format=None):
        snippets = Board.objects.all()
        serializer = BoardSerializers(snippets, many=True)
        return Response(serializer.data)
#    def post(self, request, format=None):
 #       serializer = BoardSerializers(data=request.data)
#        if serializer.is_valid():
 #           serializer.save()
  #          return Response(serializer.data, status=status.HTTP_201_CREATED)
   #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Board_change(APIView):
    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BoardSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BoardSerializers(snippet, data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   # def delete(self, request, pk, format=None):
     #   snippet = self.get_object(pk)
     #   snippet.delete()
     #   return Response(status=status.HTTP_204_NO_CONTENT)





class Onyx_view(APIView):
    def get(self, request, format=None):
        snippets = Onyx.objects.all()
        serializer = OnyxSerializers(snippets, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = OnyxSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Onyx_change(APIView):
    def get_object(self, pk):
        try:
            return Onyx.objects.get(pk=pk)
        except Onyx.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = OnyxSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = OnyxSerializers(snippet, data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 #   def delete(self, request, pk, format=None):
  #      snippet = self.get_object(pk)
   #     snippet.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)

