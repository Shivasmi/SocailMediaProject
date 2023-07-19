from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User_Profile 
import random


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST ['username']
        email = request.POST ['email']
        password = request.POST ['password']
        password_confirmation = request.POST ['password_confirmation']

        if password_confirmation == password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken, choose anotherusername')
                return redirect('signup')
            else: 
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()

            #user login 
            user_login = auth.authenticate(username=username, password=password )
            auth.login(request,user_login)

            #user registerations for a new user account 
            #user_model = User.objects.get(username=username)
            new_profile=User_Profile.objects.create(user=user)
            new_profile.save()
            messages.success(request, "user reg sucessfull ")
            return redirect('signup')
        else: 
            messages.info(request, 'password not matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
    







