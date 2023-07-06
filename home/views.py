from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from home.models import *
# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request,"home.html")
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
            return redirect('/home')
    return render(request,"signin.html")


def logout_page(request):
    logout(request)
    return redirect("/login")

def addroom(request):
 if(request.method=="POST"):
    building_name=request.POST.get("building_name")
    building=Building.objects.filter(building_name=building_name)
    room_number=request.POST.get("room_number")
    print(room_number,building[0].building_name)
    Room.objects.create(building_name=building.first(),room_number=room_number)
 queryset=Building.objects.all()
 print(queryset)
 return render(request,"addroom.html",{"queryset":queryset})

def addbuilding(request):
    if(request.method=="POST"):
        Building_name=request.POST.get("Building_name")
        Building.objects.create(building_name=Building_name)
        
    return render(request,"addbuilding.html")


def addexam(request):
    return render(request,"addexam.html")
def addinvigilator(request):
    if(request.method=="POST"):
        Invigilator_firstname=request.POST.get("first_name")
        Invigilator_lastname=request.POST.get("last_name")
        Invigilator_age=request.POST.get("age")
        Invigilator_address=request.POST.get("address")
        Invigilator_phone_number=request.POST.get("phone_number")
        Invigilator_gender=request.POST.get("gender")
        Invigilator_email=request.POST.get("email")
        print("Hello")
        Invigilator.objects.create(Invigilator_firstname=Invigilator_firstname,Invigilator_lastname=Invigilator_lastname,Invigilator_gender=Invigilator_gender,Invigilator_address=Invigilator_address,Invigilator_email=Invigilator_email,Invigilator_phone_number=Invigilator_phone_number,Invigilator_age=Invigilator_age)





    return render(request,"addinvigilator.html")

