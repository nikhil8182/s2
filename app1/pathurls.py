from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.Device_details.as_view()),
    path("<int:pk>/", views.Device_Change.as_view()),
    path("sensor/", views.Sensor_details.as_view()),
    path("sensor/<int:pk>/", views.Sensor_Change.as_view()),
    path("motion/", views.Motion_details.as_view()),
    path("motion/<int:pk>/", views.Motion_Change.as_view()),
    path("schedule/", views.Reminder.as_view()),
    path("schedule/<int:pk>/", views.Reminder_change.as_view()),
    path("tab/", views.Tab_view.as_view()),
    path("tab/<int:pk>/", views.Tab_change.as_view()),
    path("table/", views.Table_view.as_view()),
    path("table/<int:pk>/", views.Table_change.as_view()),
    path("fan/", views.Fan_view.as_view()),
    path("fan/<int:pk>/", views.Fan_change.as_view()),
    path("room/", views.Room_view.as_view()),
    path("room/<int:pk>/", views.Room_change.as_view()),
    path("user/", views.User_view.as_view()),
    path("user/<int:pk>/", views.User_change.as_view()),
    path("heater/", views.Heater_view.as_view()),
    path("heater/<int:pk>/", views.Heater_change.as_view()),
    path("board/", views.Board_view.as_view()),
    path("board/<int:pk>/", views.Board_change.as_view()),
    path("onyx/", views.Onyx_view.as_view()),
    path("onyx/<int:pk>/", views.Onyx_change.as_view()),
    path("em/", views.em_view.as_view()),
    path("em/<int:pk>/", views.em_change.as_view()),
    path("water/", views.water_view.as_view()),
    path("water/<int:pk>/", views.water_change.as_view()),
    path("led/", views.led_view.as_view()),
    path("led/<int:pk>/", views.led_change.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
