from django.contrib import admin

from .models import *

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    
    
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["id", "building","room_number"]
    list_filter = ["building",]
    search_fields = ["room_number",]


@admin.register(Invigilator)
class InvigilatorAdmin(admin.ModelAdmin):
    list_display = ["id", "fullname","email","age","gender","address","phone_number"]
    search_fields = ["firstname"]
    list_filter=["gender"]

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ["id", "name","semester_type","regular_or_back","date","shift","start_time","end_time"]
    search_fields = ["name"]
    list_filter=["semester_type"]

@admin.register(ExamHallSession)
class ExamHallSessionAdmin(admin.ModelAdmin):
    list_display = ["id", "room","shift","date"]
    list_filter=["room","shift"]

