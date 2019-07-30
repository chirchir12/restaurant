from django.shortcuts import render,redirect
from . forms import *


# Create your views here.

def login(request):
    title="Login"
    return render(request,"login_form.html",{"title":title})


def register(request):
    title="Registration"

    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            register=form.save(commit=False)
            # Save the provided password in hashed format
            register.set_password(form.cleaned_data["password2"])
            register.save()
            return redirect("/")
    else:
        form=RegisterForm()
    return render(request,"registration_form.html",{"title":title,"form":form})
