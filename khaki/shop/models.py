from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class MensCloths(models.Model):
    product_image = models.FileField(upload_to="MensCloths/",max_length=8000)
    product_category =models.CharField(default='MensCloths',max_length=50)
    product_name=models.CharField(max_length=50)
    product_price=models.CharField(max_length=50)
    product_short_description=models.CharField(max_length=100)
    product_long_description=models.CharField(max_length=500)
    product_quantity=models.IntegerField()
    slug=AutoSlugField(populate_from="product_name",unique=True,null=True,default=None)
   
    
    
    

class MensShoes(models.Model):
    product_image = models.FileField(upload_to="MensShoes/",max_length=8000)
    product_category =models.CharField(default='MensShoes',max_length=50)
    product_name=models.CharField(max_length=50)
    product_price=models.CharField(max_length=50)
    product_short_description=models.CharField(max_length=100)
    product_long_description=models.CharField(max_length=500)
    product_quantity=models.IntegerField()
    slug=AutoSlugField(populate_from="product_name",unique=True,null=True,default=None)
   
    
    

class MensWatches(models.Model):
    product_image = models.FileField(upload_to="MensWatches/",max_length=8000)
    product_category =models.CharField(default='MensWatches',max_length=50)
    product_name=models.CharField(max_length=50)
    product_price=models.CharField(max_length=50)
    product_short_description=models.CharField(max_length=100)
    product_long_description=models.CharField(max_length=500)
    product_quantity=models.IntegerField()
    slug=AutoSlugField(populate_from="product_name",unique=True,null=True,default=None)
   
    
    

class WomensHandbags(models.Model):
    product_image = models.FileField(upload_to="WomensHandbags/",max_length=8000)
    product_category =models.CharField(default='WomensHandbags',max_length=50)
    product_name=models.CharField(max_length=50)
    product_price=models.CharField(max_length=50)
    product_short_description=models.CharField(max_length=100)
    product_long_description=models.CharField(max_length=500)
    product_quantity=models.IntegerField()
    slug=AutoSlugField(populate_from="product_name",unique=True,null=True,default=None)
   
    
    

class WomensGlasses(models.Model):
    product_image = models.FileField(upload_to="WomensGlasses",max_length=8000)
    product_category =models.CharField(default='MensGlasses',max_length=50)
    product_name=models.CharField(max_length=50)
    product_price=models.CharField(max_length=50)
    product_short_description=models.CharField(max_length=100)
    product_long_description=models.CharField(max_length=500)
    product_quantity=models.IntegerField()
    slug=AutoSlugField(populate_from="product_name",unique=True,null=True,default=None)
   
    
    