from django.db import models as m
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    phone_number = m.IntegerField(null=True,blank=True)