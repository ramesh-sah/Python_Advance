from django.contrib import admin
from ChekOut.models import CheckOutDetail
# Register your models here.
class checkoutdetails(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','country','city','address','login_email','tel','mobile','ordernote','payment','slug','product_name','product_price','no_of_product_item','status']
admin.site.register(CheckOutDetail,checkoutdetails)

