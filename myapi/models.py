from django.db import models
from rx import alias

# Create your models here.
class Hero(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    alias=models.CharField(max_length=200,null=True,blank=True)