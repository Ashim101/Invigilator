from django.db import models
from autoslug import AutoSlugField


class Building(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)


    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.title

class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Faculties"

class Room(models.Model):
    
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="rooms"
    )
    room_number = models.CharField(max_length=30)
    slug=AutoSlugField(populate_from='room_number',unique=True,null=True,default=None)



    def __str__(self):
        return self.building.name + " building room " + self.room_number
    @staticmethod
    def get_available_rooms(date, shift):
        assigned_rooms= ExamHallSession.objects.filter(date=date, shift=shift).values('room')
        return Room.objects.all().exclude(id__in=assigned_rooms) 
 

    class Meta:
        unique_together = ["building", "room_number"]
        ordering = ["building__name"]


class Invigilator(models.Model):
    class GenderChoice(models.TextChoices):
        MALE = "male", "male"
        FEMALE = "female", "female"
        OTHERS = "others", "others"
    
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=7, choices=GenderChoice.choices, default=GenderChoice.MALE.value)
    address = models.CharField(max_length=255,blank=True,null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True,unique=True)
    post = models.CharField(max_length=255, blank=True,null=True)
    slug=AutoSlugField(populate_from='firstname',unique=True,null=True,default=None)


    def __str__(self):
        return self.firstname + " " + self.lastname

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
 

    @staticmethod
    def get_available_invigilator(date, shift):
        assigned_invigilators = ExamHallSession.objects.filter(date=date, shift=shift).values('invigilators')
        return Invigilator.objects.all().exclude(id__in=assigned_invigilators) 


 
class Exam(models.Model):
    
    class Semester_typeChoice(models.TextChoices):
        ODD = "Odd", "odd"
        EVEN = "Even", "Even"
    
    class RegularOrBackChoices(models.TextChoices):
        REGULAR = "Regular", "Regular"
        BACK = "Back", "Back"
    class ShiftChoice(models.TextChoices):
        MORNING = "Morning", "Morning"
        DAY = "Day", "Day"
    name = models.CharField(max_length=255)
    semester_type = models.CharField(max_length=50,choices=Semester_typeChoice.choices,default=Semester_typeChoice.ODD.value)
    regular_or_back = models.CharField(max_length=50,choices=RegularOrBackChoices.choices,default=RegularOrBackChoices.REGULAR.value)

    date = models.DateField()
    shift = models.CharField(max_length=255,choices=ShiftChoice.choices, default=ShiftChoice.DAY.value)
    start_time = models.TimeField()
    end_time = models.TimeField()
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)

    
    @staticmethod
    def get_unmanaged_exams(date, shift):
        managed_exams = ExamHallSession.objects.filter(date=date, shift=shift).values('exams')
        return Exam.objects.filter(date=date, shift=shift).exclude(id__in=managed_exams)    
    def __str__(self) -> str:
        return self.name +" "+ self.semester_type +" "+ self.regular_or_back

class ExamHallSession(models.Model):
    class ShiftChoice(models.TextChoices):
        MORNING = "Morning", "Morning"
        DAY = "Day", "Day"
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="exams"
    )
    exams = models.ManyToManyField(Exam)
    invigilators = models.ManyToManyField(Invigilator)

    shift = models.CharField(max_length=255,choices=ShiftChoice.choices)
    date = models.DateField()
    slug=AutoSlugField(populate_from='date',unique=True,null=True,default=None)



    def __str__(self):
            return self.room

    class Meta:
        ordering= ["room__building"]
        unique_together = ["room", "shift", "date"]
