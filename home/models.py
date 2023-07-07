from django.db import models

# Create your models here.

class Building(models.Model):
    building_name=models.CharField(max_length=225,blank=True,null=True)
    def __str__(self):
        return self.building_name
class Room(models.Model):
    building_name=models.ForeignKey(Building,on_delete=models.CASCADE,related_name="rooms")
    room_number=models.CharField(max_length=30)
    isOccupied=models.BooleanField(default=False)
    
    def __str__(self):
        return self.building_name.building_name+" building room "+self.room_number
    class Meta:
        unique_together=["building_name","room_number"]
        ordering=['building_name__building_name']

class Invigilator(models.Model):
    Invigilator_firstname=models.CharField(max_length=225,blank=True,null=True)
    Invigilator_lastname=models.CharField(max_length=225,blank=True,null=True)
    Invigilator_email=models.EmailField(blank=True,null=True)
    Invigilator_age=models.IntegerField(blank=True,null=True)
    Invigilator_gender=models.CharField(max_length=20,blank=True,null=True)
    Invigilator_address=models.CharField(max_length=225,blank=True,null=True)
    Invigilator_phone_number=models.CharField(max_length=225,blank=True,null=True)
    isAssigned=models.BooleanField(default=False)
    
    def __str__(self):
        return self.Invigilator_firstname+' '+self.Invigilator_lastname
    


class Exam(models.Model):
    examination_name=models.CharField(max_length=255,null=True,blank=True)
    examination_type=models.CharField(max_length=50,null=True,blank=True)
    semester_type=models.CharField(max_length=50,null=True,blank=True)
    regular_or_back=models.CharField(max_length=50,null=True,blank=True)
    building=models.ForeignKey(Building,on_delete=models.CASCADE,related_name="exams",null=True,blank=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name="exams",null=True,blank=True)
    invigilator=models.ManyToManyField(Invigilator)
    date=models.DateField(null=True,blank=True)
    start_time=models.TimeField(null=True,blank=True)
    end_time=models.TimeField(null=True,blank=True)
    def name(args):
     def __str__(self):
         return self.examination_name
     
    
    class Meta:
        unique_together=["room","start_time"]

        
    
   
    


