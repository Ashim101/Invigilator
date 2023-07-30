
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from home.views import *

urlpatterns = [
    path("home/", home, name="home"),
    path("admin/", admin.site.urls),
    path("register/", register, name="register"),
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("rooms/", rooms, name="rooms"),
    path("exams/", exams, name="exams"),
    path("buildings/", buildings, name="buildings"),
    path('summernote/', include('django_summernote.urls')),
    path("get-data/", get_data, name="get_data"),
    path("invigilators/", invigilators, name="invigillators"),
    path("examhallsessions/", examhallsessions, name="examhallsessions"),
    path("updateroom/<slug>/",update_room, name="update"),
    path("updatebuilding/<slug>/",update_building, name="update"),
    path("updateexam/<slug>/",update_exam, name="update"),
    path("updateinvigilator/<slug>/",update_invigilator, name="updateinvigilator"),
    path("updateexamhallsession/<slug>/",update_examhallsession, name="updateexamhallsession"),
    path("deleteroom/<slug>/",delete_room, name="deleteroom"),
    path("deletebuilding/<slug>/",delete_building, name="deletebuilding"),
    path("deleteinvigilator/<slug>/",delete_invigilator, name="deleteinvigilator"),
    path("deleteexam/<slug>/",delete_exam, name="deleteexam"),
    path("deleteexamhallsession/<slug>/",delete_examhallsession, name="deleteexamhallsession"),
    path("uploadcsv/", uploadcsv, name="uploadcsv"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)