from django.shortcuts import render,redirect

from .forms import UserRegister, UserLogin
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.


def home(request):

    return render (request, 'users/home.html')


def register_view(request):
    
    if request.method == 'POST':
         
        obj = UserRegister(request.POST)
        
        if obj.is_valid():
        
            username = obj.cleaned_data.get('username')
            obj.save()
            # using messages framework
            messages.success(request, "Welcome  {}, registration with success!".format(username))
            return redirect ('login-path')
        else:
            messages.warning(request,"Registration not successful,please try again ! ")

    return render (request, 'users/register.html', {'form' : UserRegister()})



def login_view(request):

    if request.method == 'POST':
        x = request.POST.get('username')
        y = request.POST.get('password')
        user = authenticate(request,username = x,password = y)
        if user :
            login(request,user)
            return redirect('home-path')
        else:
            messages.warning(request,"Username and/or password are invalid! ")


    
    return render (request, 'users/login.html',{'form' :UserLogin() })


def logout_view(request):
    
    auth.logout(request)
    
    
    return render (request, 'users/logout.html',)

def profile_view(request):


    return render(request, 'users/profile.html',{'user' : User.objects.get (username = request.user)})