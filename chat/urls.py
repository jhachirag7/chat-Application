from django.contrib import admin
from django.urls import path, re_path
from .views import index,room,public
app_name='chat'
urlpatterns = [
    path('<str:room_name>/', room, name='room'),
    path('',public,name="public")
]