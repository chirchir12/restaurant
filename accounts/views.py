from django.shortcuts import render,redirect
from . forms import *
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def login_user(request):
    title="Login"
    logout(request)
    username= password=''
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():

            username=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect("/")

            else:
                 messages.error(request,'username or password not correct')
                 return redirect('login')



    login_form=LoginForm()
    return render(request,"login_form.html",{"title":title,"form":login_form})


def register(request):
    title="Registration"

    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            register=form.save(commit=False)
            # Save the provided password in hashed format
            register.set_password(form.cleaned_data["password2"])
            register.save()
            return redirect("login")
    else:
        form=RegisterForm()
    return render(request,"registration_form.html",{"title":title,"form":form})


def logout_user(request,next_page=None):
    logout(request)

    return redirect("/")
