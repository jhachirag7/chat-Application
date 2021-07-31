# chat/views.py
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
def index(request):
    return render(request, 'chat/index.html',{})

def public(request):

    return render(request,'chat/room.html',{
         'room_name':'public'
     })

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
def chat(request):
    return render(request,'chat/chat.html',{})