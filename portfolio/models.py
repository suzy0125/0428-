from django.db import models
from django.utils import timezone
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    major = models.TextField(max_length=20)
    grade = models.IntegerField()
    hometown = models.TextField(max_length=100)

