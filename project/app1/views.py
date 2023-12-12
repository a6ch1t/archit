from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout



# Create your views here.
def home(request):
    return render(request,'base.html')

def login(request):
    form=forms.loginform()
    if request.method=='POST':
        form=forms.loginform(request.POST)
        if form.is_valid():
            form.save()
            return list(request)
        return render(request,'login.html')
    
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('cpass1')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username already exists!')
                print("alrady have")
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                return redirect(user_login)
        else:
            print('wrong password')
    return render(request,'signup.html')


    