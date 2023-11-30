from django.shortcuts import render

from app1.models import *
from app1.form import studform
# Create your views here.

def home(request):
    return render(request,'base.html')

def add_item(request):
    d=studform()
    if request.method=='POST':
        d=studform(request.POST)
        if d.is_valid():
            d.save()
            return list_item(request)
    return render(request,'add.html',{'form':d})

def list_item(request):
    p=student.objects.all()
    return render(request,'list.html',{'d':p})
