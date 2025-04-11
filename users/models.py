from django.db import models as m
from django.contrib.auth.models import AbstractUser
from .validator import *
# Create your models here.
class CustomUser(AbstractUser):
    phone_number = m.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name="شماره موبایل",
        unique=True,
        validators=[validate_iranian_phone_number])