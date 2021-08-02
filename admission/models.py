from django.db import models
from django.utils import timezone
# Create your models here.

class class_opted(models.IntegerChoices):
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
    NINTH = 9

class Student(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.IntegerField()
    mobile_number = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=50)
    class_opt = models.PositiveSmallIntegerField(choices=class_opted.choices, default=class_opted.FIFTH)
    marks = models.FloatField()
    date_enrolled = models.DateTimeField(default=timezone.now)

