from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class eeko(models.Model):
    email=models.CharField(max_length=100)
    password=models.IntegerField()


class eeeko(models.Model):
    email=models.CharField(max_length=100)
    password=models.IntegerField()


class Locate(models.Model):
    location=models.CharField(max_length=45)

class rydeinfo(models.Model):
    starting_location=models.CharField(max_length=45)
    ending_location=models.CharField(max_length=45)
    typey = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User , on_delete= models.CASCADE)
