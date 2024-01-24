from django.db import models

# Create your models here.

class eeko(models.Model):
    email=models.CharField(max_length=100)
    password=models.IntegerField()


class eeeko(models.Model):
    email=models.CharField(max_length=100)
    password=models.IntegerField()


class Locate(models.Model):
    location=models.CharField(max_length=45)