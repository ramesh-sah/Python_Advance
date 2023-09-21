from django.contrib import admin
from accounts.models import CustomUser

# Register your models here.
class ACCount(admin.ModelAdmin):
    list_display=['email','first_name','last_name','password','country','city','tel','mobile']
    
admin.site.register(CustomUser,ACCount)
