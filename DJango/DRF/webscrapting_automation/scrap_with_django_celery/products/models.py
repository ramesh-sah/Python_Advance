from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=400, unique=True)
    price = models.CharField(max_length=400, unique=True)
    description = models.TextField(unique=True)
