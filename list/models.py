from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    add  = models.CharField(max_length=200)
    cell = models.CharField(max_length=200) 

    