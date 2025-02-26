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
class UserPasswordForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ['password']
class UserNameForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ['username']
class UserEmailForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ['email']