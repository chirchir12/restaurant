from django.shortcuts import render

# Create your views here.

def login(request):
    title="Login"
    return render(request,"login_form.html",{"title":title})
