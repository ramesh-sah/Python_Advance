from django.contrib import admin
from .models import Products
# Example admin.py

# Register your models here.
admin.register(Products)


class productsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description']
