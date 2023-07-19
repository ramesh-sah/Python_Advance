from django.contrib import admin
from Refund.models import refund


# Register your models here.
class refund_page(admin.ModelAdmin):
    list_display = ('title_refund', 'description')


admin.site.register(refund, refund_page)
