from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if(request.method=="POST"):
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        exist = User.objects.filter(username=username)
        if exist.exists():
            messages.error(request, "username already exists")
            return redirect("/register/")
        user=User.objects.create(first_name=first_name,last_name=last_name,username=username) 
        user.set_password(request.POST.get("password1"))
        user.save()
        messages.info(request, "Account created successfully")

        return redirect("/register/")
    return render(request,"signup.html")
def login_page(request):
    if(request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username+password)
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"User doesnot exists")
        else:
            login(request,user)
            print("hELLO")
            return redirect('/register')
    return render(request,"signin.html")


def logout_page(request):
    logout(request)
    return redirect('/login')
