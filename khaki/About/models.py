from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class about(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug=AutoSlugField(populate_from="title",unique=True,null=True,default=None)
    
    
