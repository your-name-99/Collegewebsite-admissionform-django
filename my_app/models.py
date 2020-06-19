from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
# Create your models here.
class student(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.IntegerField()
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    course=models.CharField(max_length=20)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    hobbies=models.CharField(max_length=50)
    address=models.CharField(max_length=200)