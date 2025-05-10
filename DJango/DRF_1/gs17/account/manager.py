from django.db import models
from django.contrib.auth.models import BaseUserManager

#custom user manager
class UserManager(BaseUserManager):
    def create_user(self,email,name,tc, password=None, password2=None):
        if not email:
            raise ValueError("User Must Have an email address")
        user=self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,tc,password=None):
        user=self.create_user(email,password=password,name=name,tc=tc,)
        user.is_admin=True
        user.save(using=self._db)
        return user
    
    
    