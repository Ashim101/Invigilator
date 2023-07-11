import json
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
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
            Q(fullname__icontains=search)|
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


@login_required(login_url="/login/")
def get_data(request):
    date = request.GET.get('date')
    shift = request.GET.get('shift')
    
    # Perform necessary logic based on the selected option
    # Generate the updated options for the dependent dropdowns
    # exams = Exam.objects.filter( ~Q(Exam.is_managed(self,date,shift)))    

    # examsession=examhallsessions.objects.filter(date=date,shift=shift)
    # exams=examsession.exams.all().values_list("exams__id")
    
    
    
    
           
    
    exams=Exam.get_unmanaged_exams(date=date,shift=shift)
    invigilators=Invigilator.get_available_invigilator(date=date,shift=shift)
    rooms=Room.get_available_rooms(date=date,shift=shift)
    rooms = [{"name": f' {room.building} building room {room.room_number}'} for room in rooms]
    invigilators = [{"name": f' {invigilator.fullname} {invigilator.gender}  {invigilator.age} semester'} for invigilator in invigilators]
    
    

    

    # exams = Exam.objects.filter( ~Q(examhallsession__date=date, examhallsession__shift=shift))    
    exams = [{"name": f' {exam.regular_or_back} {exam.name}  {exam.semester_type} semester'} for exam in exams]
    print(exams)
    print(invigilators)
    print(rooms)

    return JsonResponse({"exams":exams,"invigilators":invigilators,"rooms":rooms}, safe=False)

    
    # options1 = [{'value': 'option1', 'label': 'Option 1'}, {'value': 'option2', 'label': 'Option 2'}]
    # options2 = [{'value': 'option3', 'label': 'Option 3'}, {'value': 'option4', 'label': 'Option 4'}]
    
    # data = {
    #     'options1': options1,
    #     'options2': options2,

    # }
    
    # return JsonResponse(data)
    # return JsonResponse(list(rooms.values()), safe=False)


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

        
        form = RoomForm()
        room_qs = Room.objects.all()
        context = {
        "form":form,
        "rooms":room_qs
        }
        return render(request, "room.html",context=context)

        
    context = {
        "form":form,
    }
    return render(request, "updateroom.html",context=context)


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

        
        form = BuildingForm()
        building_qs = Building.objects.all()
        context = {
        "form":form,
        "buildings":building_qs
        }
        return render(request, "building.html",context=context)

        
    context = {
        "form":form,
    }
    return render(request, "updatebuilding.html",context=context)



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

        
        form = ExamForm()
        updateexam_qs = Exam.objects.all()
        context = {
        "form":form,
        "exams":updateexam_qs
        }
        return render(request, "exam.html",context=context)
    context = {
    "form":form,
    }
    return render(request, "updateexam.html",context=context)
    



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

        
        form = InvigilatorForm()
        invigilator_qs = Invigilator.objects.all()
        context = {
        "form":form,
        "invigilators":invigilator_qs
        }
        return render(request, "updateinvigilator.html",context=context)



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

        
        form = ExamHallSessionForm()
        examhallsession_qs = ExamHallSession.objects.all()
        context = {
        "form":form,
        "examhallsessions":examhallsession_qs
        }
        return render(request, "updateexamhallsession.html",context=context)


def delete_room(request,slug):
    Room.objects.get(slug=slug).delete()
    


        
    form = RoomForm()
    room_qs = Room.objects.all()
    context = {
    "form":form,
    "rooms":room_qs
    }
    return render(request, "room.html",context=context)

def delete_building(request,slug):
    Building.objects.get(slug=slug).delete()
    


        
    form = BuildingForm()
    building_qs = Building.objects.all()
    context = {
    "form":form,
    "buildings":building_qs
    }
    return render(request, "building.html",context=context)


def delete_exam(request,slug):
    Exam.objects.get(slug=slug).delete()
    


        
    form = ExamForm()
    exam_qs = Exam.objects.all()
    context = {
    "form":form,
    "exams":exam_qs
    }
    return render(request, "exam.html",context=context)
