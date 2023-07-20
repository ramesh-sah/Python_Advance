from django.db import models


# Create your models here.
class savehome(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=56)
    phone = models.CharField(max_length=55)
    address = models.CharField(max_length=56)
    message = models.CharField(max_length=54)
