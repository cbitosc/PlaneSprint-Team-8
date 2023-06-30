from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_protect
import os


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Registration successful. You can now login.')
            return redirect('login')  # Replace 'login' with your desired redirect URL after successful registration
    
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')  # Replace 'home' with your desired redirect URL after successful login
        else:
            # messages.error(request, 'Invalid username or password.')
            return render(request,'login.html',{'message' : 'Invalid credentials',})
    
    return render(request, 'login.html')

def logout_view(request) :
    logout(request)
    return redirect('home')

