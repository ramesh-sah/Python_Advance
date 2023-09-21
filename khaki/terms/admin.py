from django.contrib import admin
from terms.models import Terms
# Register your models here.
class TermCondition(admin.ModelAdmin):
    list_display = ('title',"description",'slug')

admin.site.register(Terms, TermCondition)

