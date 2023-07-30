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
        
class InvigilatorUploadForm(forms.Form):
    csv_file = forms.FileField()
    
from django import forms
from django.core.validators import FileExtensionValidator

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(
        label='Choose Excel File', 
        validators=[FileExtensionValidator(allowed_extensions=['xlsx'])]
    )