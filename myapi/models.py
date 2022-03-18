from tkinter import CASCADE
from django.db import models
from matplotlib.cbook import maxdict
from rx import alias

# Create your models here.
class Hero(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    alias=models.CharField(max_length=200,null=True,blank=True)

class Details(models.Model):
    name=models.ForeignKey(Hero,on_delete=CASCADE)
    hobbies=models.CharField(max_length=255,null=True,blank=True)
    age=models.IntegerField()
    check=models.BooleanField()
    gender=models.CharField(max_length=200,null=True,blank=True)
    def __str__ (self):
      return f'name{self.name}'


class Department(models.Model):
    school=models.CharField(max_length=200,blank=True,null=True)
    postion=models.CharField(max_length=200,blank=True,null=True)
    course=models.CharField(max_length=255,blank=True)
    attendance=models.TextField(max_length=255,blank=True,null=True)
    def __str__(self):
        return f'school{self.school}'