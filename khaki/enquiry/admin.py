from django.contrib import admin
from enquiry.models import Enquiry

# Register your models here.
class CustomerEnquiry(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email', 'message', 'created_at', 'updated_at','slug')
admin.site.register(Enquiry,CustomerEnquiry)
