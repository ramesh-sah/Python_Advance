from django.contrib import admin
from signupdata.models import User

# Register your models here.


class Users(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')


admin.site.register(User, Users)
