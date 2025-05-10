from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from . manager import UserManager

# Create your models here.

class User(AbstractBaseUser):
    email=models.EmailField(verbose_name='email',
                            max_length=255,
                            unique=True)
    name=models.CharField(max_length=200)
    tc=models.BooleanField()
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name','tc']
    
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin
    
    
    
