from django.db import models

# Create your models here.
class CheckOutDetail(models.Model):
    first_name = models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    email=models.EmailField(max_length=69)
    country=models.CharField(max_length=54)
    city=models.CharField(max_length=76)
    address=models.CharField(max_length=34)
    login_email=models.EmailField(max_length=76)
    tel=models.CharField(max_length=43)
    mobile=models.CharField(max_length=76)
    ordernote=models.CharField(max_length=76,default="None")
    payment=models.CharField(max_length=54)
    slug=models.CharField(max_length=34,default="checkoutall")
    product_name=models.CharField(max_length=65)
    no_of_product_item=models.IntegerField(default='0')
    product_price=models.CharField(max_length=76)
    created_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=34,default="pending")


