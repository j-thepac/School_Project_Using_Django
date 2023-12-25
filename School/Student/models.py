from django.db import models

# Create your models here.


class Student(models.Model):
    id:int=models.IntegerField(primary_key=True)
    name:str=models.CharField(max_length=100)
    age:int=models.IntegerField()
    classStudent:str=models.CharField(max_length=100)
