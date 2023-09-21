from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Refund(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    slug=AutoSlugField(populate_from="title",unique=True,null=True,default=None)
    
