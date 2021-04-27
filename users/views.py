from django.shortcuts import render,redirect

from .forms import UserRegister
from django.contrib.auth.models import User

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