from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    student_class = models.IntegerField()
    city = models.CharField(max_length=50)

    def  __str__(self):
        return self.name

    class Meta:
        db_table = 'stinfo'
        ordering = ['-name']


class StudentLogin(models.Model):
    user_id =  models.CharField(max_length=50,  unique=True)
    password =  models.CharField(max_length=50)
    name = models.CharField(max_length=50, null=True)
    
    def  __str__(self):
        return self.name


class CityDetails(models.Model):
    state_id =  models.CharField(max_length=50)
    city_name =  models.CharField(max_length=100)
        
    def  __str__(self):
        return self.city_name    
    