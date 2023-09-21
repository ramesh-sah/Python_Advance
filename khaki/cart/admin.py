from django.contrib import admin
from cart.models import Cart

# Register your models here.
class CART(admin.ModelAdmin):
    list_display = ['product_name','description','product_price','no_of_product_item','customer_email','slug']

admin.site.register(Cart,CART)