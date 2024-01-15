from django.shortcuts import render

# Create your views here.

from .models import *
from app1.form import *
def home(request):
    return render(request,'index.html')