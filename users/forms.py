from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegister(UserCreationForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email',]


# class UserLogin(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput())


class UserLogin(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','password']
    