"""
URL configuration for invigilator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from home.views import *

urlpatterns = [
    path("", home, name="home"),
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
    path("deleteexam/<slug>/",delete_exam, name="deleteexam"),








]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)