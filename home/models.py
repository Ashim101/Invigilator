from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="rooms"
    )
    room_number = models.CharField(max_length=30)

    def __str__(self):
        return self.building.name + " building room " + self.room_number

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
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=7, choices=GenderChoice.choices, default=GenderChoice.MALE.value)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Exam(models.Model):
    name = models.CharField(max_length=255)
    semester_type = models.CharField(max_length=50)
    regular_or_back = models.CharField(max_length=50)

    date = models.DateField()
    shift = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()


class ExamHallSession(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="exams", null=True, blank=True
    )
    exams = models.ManyToManyField(Exam)
    invigilator = models.ManyToManyField(Invigilator)    

    shift = models.CharField(max_length=255)
    date = models.DateField()

    def name(args):
        def __str__(self):
            return self.examination_name

    class Meta:
        unique_together = ["room", "shift", "date"]
