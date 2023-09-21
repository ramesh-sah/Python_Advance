from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *


# Create your models here.

class CustomUser(AbstractUser):
    
    username=None
    email=models.EmailField(unique=True)
    profile_image=models.FileField(upload_to='profile/', blank=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    tel=models.CharField(max_length=60)
    mobile=models.CharField(max_length=15)
    
    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    



    