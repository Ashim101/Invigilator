import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render

from home.models import *
from .forms import BuildingForm, RoomForm, InvigilatorForm, ExamForm


# Create your views here.
@login_required(login_url="/login/")
def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        exist = User.objects.filter(username=username)
        if exist.exists():
            messages.error(request, "username already exists")
            return redirect("/register/")
        user = User.objects.create(
            first_name=first_name, last_name=last_name, username=username
        )
        user.set_password(request.POST.get("password1"))
        user.save()
        messages.info(request, "Account created successfully")

        return redirect("/register/")
    return render(request, "signup.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username + password)
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "User doesnot exists")
        else:
            login(request, user)
            return redirect("/home")
    return render(request, "signin.html")


def logout_page(request):
    logout(request)
    return redirect("/login")


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
           form.save()
    return render(request, "room.html",context=context)

@login_required(login_url="/login/")
def exams(request):
    form = ExamForm()
    queryset = Exam.objects.all()
    context = {
        "form":form,
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
def examseddions(request):
    form = examseddionForm()
    queryset = examseddion.objects.all()
    context = {
        "form":form,
        "examseddions":queryset
    }
    if request.method == "POST":
        form=examseddionForm(request.POST)
        if form.is_valid():
           form.save()

    return render(request, "examseddion.html",context=context)


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
