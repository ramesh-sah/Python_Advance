from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Enquiry(models.Model):
    first_name = models.CharField(max_length=60,null=True, blank=True)
    last_name = models.CharField(max_length=60,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug=AutoSlugField(populate_from="first_name",unique=True,null=True,default=None)
    
    
