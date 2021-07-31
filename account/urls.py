from django.contrib import admin
from django.urls import path, re_path
from .views import register,login
urlpatterns = [
    path('register',register,name="register"),
    path('login',login,name='login')
]

