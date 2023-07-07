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
   pass    
    


