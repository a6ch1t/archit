from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from app1.models import *
from .form import *

# Create your views here.

from .models import *
from app1.form import *

def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')




def signup(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('pass2')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'useername already exists!')
                print("Already Have")
                return redirect(signup)
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                return redirect(user_login)
        else:
            print("wrong Password")
    return render(request,'signup.html')
    

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        user=authenticate(request,username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(index)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(user_login)
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect(user_login)

def cart(request):
    return render(request,'cart.html')


def destination(request):
    l=Locate.objects.all()


    return render(request,'destination.html',{'locate':l})
