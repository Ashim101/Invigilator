import json
import csv
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import  login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
import pandas as pd


from home.models import *
from .forms import BuildingForm, RoomForm, InvigilatorForm, ExamForm,ExamHallSessionForm,InvigilatorUploadForm,ExcelUploadForm

# Create your views here.
def home(request):
    # examhallsession_qs = ExamHallSession.objects.all()
    # building=Building.objects.all()
    # return render(request,"home.html",{"examhallsessions":examhallsession_qs,"buildings":building} )
    buildings = Building.objects.all()
    building_exam_data = []

    for building in buildings:
        examhallsession_qs = ExamHallSession.objects.filter(room__building=building)
        building_data = {
            'building': building,
            'examhallsessions': examhallsession_qs,
        }
        if examhallsession_qs.count()>=1:
           building_exam_data.append(building_data)

    return render(request, "home.html", {"building_exam_data": building_exam_data})

def register(request):
    form=UserCreationForm()
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
          form.save()
          messages.success(request,"Account created successfully")
          return HttpResponseRedirect(reverse("login"))
        else:
          messages.error(request,"Account not created! please try again")
        
    return render(request,"signup.html",{
        "form":form,
    })
        
    
 


def login_page(request):
    if request.method == "POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return HttpResponseRedirect(reverse("home"))
        else:
            messages.error(request,"Login failed please check the username and password again")
    return render(request,"signin.html")



def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))



@login_required(login_url="/login/")
def buildings(request):
    form = BuildingForm()
    building_qs = Building.objects.all()
    if request.GET.get("search"):
        search= request.GET.get("search")
        building_qs=building_qs.filter(
            Q(name__icontains=search)

            )
    context = {
        "form":form,
        "buildings":building_qs
    }
    if request.method == "POST":
        form=BuildingForm(request.POST)
        if form.is_valid():
           form.save()

    return render(request, "building.html",context=context)


@login_required(login_url="/login/")
def rooms(request):
    form = RoomForm()
    room_qs = Room.objects.all()
    if request.GET.get("search"):
        search= request.GET.get("search")
        room_qs=room_qs.filter(
            Q(room_number__icontains=search)|
            Q(building__name__icontains=search)

            )
    context = {
        "form":form,
        "rooms":room_qs
    }
    if request.method == "POST":
        form=RoomForm(request.POST)
        if form.is_valid():
            try:
              form.save()
            except:
               messages.error(request,"This room is already in the list")   
        else:
            messages.error(request,"This room is already in the list")
    return render(request, "room.html",context=context)

@login_required(login_url="/login/")
def exams(request):
    form = ExamForm()
    exam_qs = Exam.objects.all()
    if request.GET.get("search"):
        search= request.GET.get("search")
        exam_qs=exam_qs.filter(
            Q(name__icontains=search)|
            Q(semester_type__icontains=search)|
            Q(date__icontains=search)|
            Q(regular_or_back__icontains=search)



            )
    context = {
        "form":form,
        "exams":exam_qs
    }
    if request.method == "POST":
        form=ExamForm(request.POST)
        if form.is_valid():
           form.save()

    return render(request, "exam.html",context=context)

@login_required(login_url="/login/")
def invigilators(request):
    form = InvigilatorForm()
    invigilator_qs = Invigilator.objects.all()
    if request.GET.get("search"):
        search= request.GET.get("search")
        invigilator_qs=invigilator_qs.filter(
            Q(firstname__icontains=search)|
            Q(lastname__icontains=search)|
            Q(age__icontains=search)|
            Q(gender__icontains=search)|
            Q(address__icontains=search)|
            Q(phone_number__icontains=search)




            )
    context = {
        "form":form,
        "invigilators":invigilator_qs
    }
    if request.method == "POST":
        form=InvigilatorForm(request.POST)
        if form.is_valid():
            try:
               form.save()
               messages.success(request,"Details saved successfully")
            except:
                messages.success(request,"Internal error")
        else:
            messages.error(request,"Person with this emal already exist")

            


    return render(request, "invigilator.html",context=context)

@login_required(login_url="/login/")
def examhallsessions(request):
    form = ExamHallSessionForm()
    examhallsession_qs = ExamHallSession.objects.all()
    if request.GET.get("search"):
        search= request.GET.get("search")
        examhallsession_qs=examhallsession_qs.filter(
            Q(exams__name__icontains=search)|
            Q(invigilators__firstname__icontains=search)|
            Q(date__icontains=search)
            )
    context = {
        "form":form,
        "examhallsessions":examhallsession_qs
    }
    if request.method == "POST":
        form=ExamHallSessionForm(request.POST)
        try:
           if form.is_valid():
            messages.success(request,"Details saved successfully")
            form.save()
           else:
                messages.error(request,"Form not valid error")
        
        except:
            messages.error(request,"Internal error")

    return render(request, "examhallsession.html",context=context)


@login_required(login_url="/login/")
def get_data(request):
    date = request.GET.get('date')
    shift = request.GET.get('shift')
    

    from django.db.models import F
    exams=Exam.get_unmanaged_exams(date=date,shift=shift).values("id", "name")
    invigilators=Invigilator.get_available_invigilator(date=date,shift=shift).annotate(name=F("firstname")).values("id", "name")
    rooms=Room.get_available_rooms(date=date,shift=shift).annotate(name=F("room_number")).values("id", "name")

    context = {
        "exams": list(exams),
        "invigilators": list(invigilators),
        "rooms": list(rooms)
    }
    

    


    return JsonResponse(context, safe=False)

    


def update_room(request,slug):
    form = RoomForm(instance=Room.objects.get(slug=slug))
    
    

    if request.method == "POST":
        form=RoomForm(request.POST,instance=Room.objects.get(slug=slug))
        if form.is_valid():
            try:
              form.save()
            except:
               messages.error(request,"This room is already in the list")   
        else:
            messages.error(request,"This room is already in the list")
        return redirect("/rooms/")
    return render(request,"updateroom.html",{"form":form})

        



def update_building(request,slug):
    form = BuildingForm(instance=Building.objects.get(slug=slug))
    
    

    if request.method == "POST":
        form=BuildingForm(request.POST,instance=Building.objects.get(slug=slug))
        if form.is_valid():
            try:
              form.save()
            except:
               messages.error(request,"This building  is already in the list")   
        else:
            messages.error(request,"This building is already in the list")
        return redirect("/buildings/")
    return render(request,"updatebuilding.html",{"form":form})


        

        




def update_exam(request,slug):
    form = ExamForm(instance=Exam.objects.get(slug=slug))
    
    

    if request.method == "POST":
        form=ExamForm(request.POST,instance=Exam.objects.get(slug=slug))
        if form.is_valid():
            try:
              form.save()
            except:
               messages.error(request,"This updateexam is already in the list")   
        else:
            messages.error(request,"This updateexam is already in the list")
        return redirect("/exams/")
    return render(request,"updateexam.html",{"form":form})

        
  

    



def update_invigilator(request,slug):
    form = InvigilatorForm(instance=Invigilator.objects.get(slug=slug))
    
    

    if request.method == "POST":
        form=InvigilatorForm(request.POST,instance=Invigilator.objects.get(slug=slug))
        if form.is_valid():
            try:
              form.save()
            except:
               messages.error(request,"This invigilator is already in the list")   
        else:
            messages.error(request,"This invigilator is already in the list")

        
        return redirect("/invigilators/")

    return render(request, "updateinvigilator.html",{"form":form})
    



def update_examhallsession(request,slug):
    form = ExamHallSessionForm(instance=ExamHallSession.objects.get(slug=slug))
    
    

    if request.method == "POST":
        form=ExamHallSessionForm(request.POST,instance=ExamHallSession.objects.get(slug=slug))
        if form.is_valid():
            try:
              form.save()
            except:
               messages.error(request,"This examhallsession is already in the list")   
        else:
            messages.error(request,"This examhallsession is already in the list")
            
        return redirect("/examhallsessions/")
    return render(request, "updateexamhallsession.html",{"form":form})


def delete_room(request,slug):
    Room.objects.get(slug=slug).delete()
    
    return redirect("/rooms/")


def delete_building(request,slug):
    Building.objects.get(slug=slug).delete()

    return redirect("/rooms/")



def delete_exam(request,slug):
    Exam.objects.get(slug=slug).delete()
    return redirect("/exams/")
def delete_invigilator(request,slug):
    Invigilator.objects.get(slug=slug).delete()
    return redirect("/invigilators/")

def delete_examhallsession(request,slug):
    ExamHallSession.objects.get(slug=slug).delete()
    return redirect("/examhallsessions/")

def uploadcsv(request):

        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)
            if 'email' not in df.columns:
                # If the 'email' column is not present in the DataFrame, set email to None for all invigilators
                df['email'] = None
            if 'address' not in df.columns:
                # If the 'address' column is not present in the DataFrame, set address to None for all invigilators
                df['address'] = None            
            if 'post' not in df.columns:
                # If the 'post' column is not present in the DataFrame, set post to None for all invigilators
                df['post'] = None

            for index, row in df.iterrows():
                
                try:
                   firstname = row['firstname']
                   lastname = row['lastname']
                   email = row['email']
                   gender = row['gender']
                   address = row['address']
                   phone_number = row['phone_number']
                   post=row['post']
                except:
                    messages.error(request,"File must contains first name,last name,phone_number and gender")
                    return redirect("/uploadcsv/") 


                    
                
                try:
                 Invigilator.objects.create(
                    firstname=firstname,
                    lastname=lastname,
                    email=email,
                    gender=gender,
                    address=address,
                    phone_number=phone_number,
                    post=post
                    
                )
                except:
                    messages.error(request,"The provided phone number is alread registered")
                    return redirect("/uploadcsv/") 



            return redirect("/invigilators/") 

        else:
         form = ExcelUploadForm()
         return render(request, 'addcsv.html', {'form': form})