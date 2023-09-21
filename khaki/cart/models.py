from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
CustomUser=get_user_model()

# Create your models here.
class Cart(models.Model):
    product_image=models.FileField(upload_to="cartImages/", blank=True, null=True,max_length=5000)
    product_name= models.CharField(max_length=100)
    description = models.TextField()
    product_price= models.CharField(max_length=50000)
    no_of_product_item=models.IntegerField(default=1,null=True,blank=True)
    customer_email= models.CharField(max_length=500)
    slug=AutoSlugField(populate_from="product_name",unique=True,null=True,default=None)
    
    
