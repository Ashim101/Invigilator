import json
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import redirect, render

from home.models import *
from .forms import BuildingForm, RoomForm, InvigilatorForm, ExamForm,ExamHallSessionForm

# Create your views here.
@login_required(login_url="/login/")
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("signin"))
    return render(request,"home.html",{
        "variable": request.user
    }
        
    )

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj=form.save()
        return HttpResponseRedirect(reverse("login"))
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
            return render(request, "signin.html",{
                "message": "Not the vaild credentials"
            })
    return render(request,"signin.html")
    #     username = request.POST.get("username")
    #     password = request.POST.get("password")
    #     print(username + password)
    #     user = authenticate(username=username, password=password)
    #     if user is None:
    #         messages.error(request, "User doesnot exists")
    #     else:
    #         login(request, user)
    #         return redirect("/home")
    # return render(request, "signin.html")


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


# @login_required(login_url="/login/")
# def addroom(request):
#     if request.method == "POST":
#         building_name = request.POST.get("building_name")
#         building = Building.objects.filter(building_name=building_name)
#         room_number = request.POST.get("room_number")
#         try:
#             Room.objects.create(building_name=building.first(), room_number=room_number)
#         except:
#             messages.error(request, "This room is already in the list {}")
#     queryset = Building.objects.all()
#     addedrooms = Room.objects.all()
#     return render(request, "addroom.html", {"queryset": queryset, "Rooms": addedrooms})


@login_required(login_url="/login/")
def buildings(request):
    form = BuildingForm()
    building_qs = Building.objects.all()
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
    queryset = Exam.objects.all()
    context = {
        "exams":queryset
    }
    if request.method == "POST":
        form=ExamForm(request.POST)
        if form.is_valid():
           form.save()

    return render(request, "exam.html",context=context)

@login_required(login_url="/login/")
def invigilators(request):
    form = InvigilatorForm()
    queryset = Invigilator.objects.all()
    context = {
        "form":form,
        "invigilators":queryset
    }
    if request.method == "POST":
        form=InvigilatorForm(request.POST)
        if form.is_valid():
           form.save()

    return render(request, "invigilator.html",context=context)

@login_required(login_url="/login/")
def examhallsessions(request):
    form = ExamHallSessionForm()
    queryset = ExamHallSession.objects.all()
    context = {
        "form":form,
        "Examsssions":queryset
    }
    if request.method == "POST":
        form=ExamHallSessionForm(request.POST)
        if form.is_valid():
           form.save()

    return render(request, "examhallsession.html",context=context)


# @login_required(login_url="/login/")
# def addexam(request):
#     building = request.GET.get("building", None)
#     rooms = None
#     if building:
#         rooms = Room.objects.filter(
#             building_name__building_name=building, isOccupied=False
#         )
#     invigilator_query = Invigilator.objects.filter(isAssigned=False)
#     building_query = Building.objects.all()
#     return render(request, "addexam.html", locals())


# @login_required(login_url="/login/")
# def get_rooms(request):
#     building = request.GET.get("building", None)
#     rooms = Room.objects.filter(building_name__building_name=building, isOccupied=False)
#     return render(request, "dropdown_list_opions.html", {"rooms": rooms})
#     # return JsonResponse(list(rooms.values()), safe=False)


# @login_required(login_url="/login/")
# def addinvigilator(request):
#     if request.method == "POST":
#         Invigilator_firstname = request.POST.get("first_name")
#         Invigilator_lastname = request.POST.get("last_name")
#         Invigilator_age = request.POST.get("age")
#         Invigilator_address = request.POST.get("address")
#         Invigilator_phone_number = request.POST.get("phone_number")
#         Invigilator_gender = request.POST.get("gender")
#         Invigilator_email = request.POST.get("email")
#         Invigilator.objects.create(
#             Invigilator_firstname=Invigilator_firstname,
#             Invigilator_lastname=Invigilator_lastname,
#             Invigilator_gender=Invigilator_gender,
#             Invigilator_address=Invigilator_address,
#             Invigilator_email=Invigilator_email,
#             Invigilator_phone_number=Invigilator_phone_number,
#             Invigilator_age=Invigilator_age,
#         )

#     return render(request, "addinvigilator.html")
