from django.contrib import admin
from submitcontact.models import submitContact


# Register your models here.
class Contact_Enquery(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'message', 'created_at', 'updated_at')


admin.site.register(submitContact, Contact_Enquery)
