from django.shortcuts import render,redirect

from .forms import UserRegister, UserLogin
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login

# Create your views here.


def home(request):

    return render (request, 'users/home.html')


def register_view(request):
    
    if request.method == 'POST':
         
        obj = UserRegister(request.POST)

        if obj.is_valid():
            obj = obj.save(commit=False)
            x = request.POST.get('email')
            obj.email = x
            obj.save()
            return redirect ('home-path')

    return render (request, 'users/register.html', {'form' : UserRegister()})



def login_view(request):

    if request.method == 'POST':
        x = request.POST.get('username')
        y = request.POST.get('password')
        user = authenticate(request,username = x,password = y)
        if user :
            login(request,user)
            return redirect('home-path')

    
    return render (request, 'users/login.html',{'form' :UserLogin() })


def logout_view(request):
    
    auth.logout(request)
    
    
    return render (request, 'users/logout.html',)