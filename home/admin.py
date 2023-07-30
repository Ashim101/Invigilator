from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


class RoomInline(admin.TabularInline):
    model = Room
    extra = 1

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    inlines = [RoomInline,]

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
    list_display = ["id", "fullname","email","gender","address","phone_number"]
    search_fields = ["firstname"]
    list_filter=["gender"]

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ["id", "name","semester_type","regular_or_back","date","shift","start_time","end_time"]
    search_fields = ["name"]
    list_filter=["semester_type"]

@admin.register(ExamHallSession)
class ExamHallSessionAdmin(admin.ModelAdmin):
    list_display = ["id", "room","shift","date","exams_name"]
    def exams_name(self,obj):
       return ', '.join([exam.name for exam in obj.exams.all()])
            
        
        
    list_filter=["room","shift"]
    filter_horizontal = ["exams", "invigilators"]


@admin.register(Notice)
class NoticeAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ["id", "title", "published_date"]
    search_fields = ["title"]
    summernote_fields = '__all__'
