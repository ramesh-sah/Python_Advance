from django.contrib import admin
from saveHome.models import savehome

# Register your models here.


class FormHome(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'message')


admin.site.register(savehome, FormHome)
