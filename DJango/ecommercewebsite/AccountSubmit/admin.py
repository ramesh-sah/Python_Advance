from django.contrib import admin
from AccountSubmit.models import Accountsubmit

# Register your models here.


class Account(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'company_name',
                    'country', 'city', 'address', 'tel_no', 'phone_no')


admin.site.register(Accountsubmit, Account)
