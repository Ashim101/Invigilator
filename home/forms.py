from django import forms
from .models import Building, Room, Invigilator, Exam,ExamHallSession

class BuildingForm(forms.ModelForm):
    class Meta:
        model=Building
        fields=("id","name")


class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields="__all__"


class InvigilatorForm(forms.ModelForm):
    class Meta:
        model=Invigilator
        fields="__all__"


class ExamForm(forms.ModelForm):
    class Meta:
        model=Exam
        fields="__all__"
class ExamHallSessionForm(forms.ModelForm):
    class Meta:
        model=ExamHallSession
        fields="__all__"