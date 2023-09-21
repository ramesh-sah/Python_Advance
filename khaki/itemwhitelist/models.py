from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class WhiteList(models.Model):
    product_name=models.CharField(max_length=100)
    product_image=models.FileField(upload_to='whitelist_images/',max_length=5000)
    customer_email=models.EmailField(max_length=300)
    product_price=models.CharField(max_length=60)
    slug=AutoSlugField(populate_from="product_name",unique=True,null=True,default=None)
