from django import forms
from managements.models import *
from django.contrib.auth.models import User
class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username','password','email']
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']