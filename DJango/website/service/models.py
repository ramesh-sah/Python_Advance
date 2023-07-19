from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Service(models.Model):
    Home_title = models.CharField(max_length=50)
    Home_desc = HTMLField()
