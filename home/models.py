from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete= models.CASCADE)
    level = models.CharField(max_length= 300)
    course = models.CharField(max_length= 300)
    category = models.CharField(max_length= 300)
    datetime = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name_plural = 'Attendance'
        
    def __str__ (self):
        return str(self.student.last_name) + " >> " + str(self.category) + " >> " + str(self.course) +  " >> " + str(self.datetime)[:19]
        # return f"{self.student.last_name } / {self.course} / {self.datetime}"
    


    
class Level(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
            verbose_name_plural = 'Categories'
            
    def __str__(self):
        return self.name
    
        