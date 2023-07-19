from django.contrib import admin
from service.models import Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('Home_title', 'Home_desc')


admin.site.register(Service, ServiceAdmin)
