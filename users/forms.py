from django import forms
from .models import *
from django.contrib.auth.models import User
class NewBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "" 
class UserRegisterForm(NewBaseForm):
    class Meta:
        model=CustomUser
        fields = ['username','email','phone_number','password']
class UserLoginForm(NewBaseForm):
    class Meta:
        model = User
        fields = ['username','password']
class UserPasswordForm(NewBaseForm):
    class Meta :
        model = CustomUser
        fields = ['password']
class UserNameForm(NewBaseForm):
    class Meta :
        model = CustomUser
        fields = ['username']
class UserEmailForm(NewBaseForm):
    class Meta :
        model = CustomUser
        fields = ['email']