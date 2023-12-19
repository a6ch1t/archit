from django.db import models

# Create your models here.
class details(models.Model):
    email=models.CharField(max_length=100)
    password=models.IntegerField()
    

class order(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=25)
    location=models.CharField(max_length=100)
    title=models.CharField(max_length=100)


    
