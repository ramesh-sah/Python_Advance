from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Accountsubmit(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    tel_no = models.CharField(max_length=15)
    phone_no = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
