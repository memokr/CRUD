from django.db import models
from django.forms import ModelForm, Textarea
# Create your models here.

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    name_of_book = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)

class Meta:
    db_table = "students"