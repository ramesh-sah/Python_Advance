from django.contrib import admin
from itemwhitelist.models import WhiteList
# Register your models here.
class whiteListedItem(admin.ModelAdmin):
    list_display = ['product_name','product_image','customer_email']

admin.site.register(WhiteList,whiteListedItem)