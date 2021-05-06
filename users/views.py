from django.shortcuts import render,redirect

from .forms import UserRegister, UserLogin
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login
from django.contrib import messages

from .forms import ProfileForm , UserForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests

# Create your views here.


def home(request):

    return render (request, 'users/home.html')


def register_view(request):

    if request.method == 'POST':
         
        obj = UserRegister(request.POST)
        
        if obj.is_valid():
            # get the 2 keys from settings.py and register POST form

            response = request.POST.get('g-recaptcha-response')
            secret = settings.GOOGLE_RECAPTCHA_SECRET_KEY

            data = {'response' : response , 'secret' : secret}

            #verification using google RECAPTCHA api and "requests" python library

            data_response = requests.post('https://www.google.com/recaptcha/api/siteverify', data = data)
            data_response = data_response.json()
            if data_response['success']:
        
                username = obj.cleaned_data.get('username')
                obj.save()
                # using messages framework
                messages.success(request, "Welcome  {}, registration with success!".format(username))
                return redirect ('login-path')
            else:
                messages.warning(request,"Invalid Recaptcha ! ")
                return redirect ('register-path')
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



@login_required(login_url = 'login-path')
def profile_view(request):

    return render(request, 'users/profile.html',{'user' : User.objects.get (username = request.user)})

@login_required(login_url = 'login-path')
def edit_profile_view(request):
    
    if request.method == 'POST':
        obj1 = UserForm(request.POST, instance = User.objects.get(username = request.user))
        obj2 = ProfileForm(request.POST, request.FILES, instance = Profile.objects.get(user = request.user))

        #print ("#################################", type(request.FILES),"#####################")

        if obj1.is_valid() and obj2.is_valid():
            obj1 = obj1.save()
            obj2 = obj2.save(commit = False)
            obj2.user = request.user
            obj2.save()
            return redirect('profile-path')

    return render(request, 'users/edit_profile.html',{'userForm' : UserForm(instance = User.objects.get(username = request.user)) ,
     'profile' : ProfileForm(instance = Profile.objects.get(user = request.user)),
     'user' : User.objects.get (username = request.user)
     })