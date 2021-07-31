from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.warning(request,"Username Taken")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'Email Taken')
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,password=password,email=email)
            user.save()
            return redirect('login')   
    else:
        return render(request,'chat/index.html',{})
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/chat/')
        else:
            messages.warning(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'chat/login.html',{})

        