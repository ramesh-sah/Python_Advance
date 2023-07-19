from django.contrib import admin
from termsConditions.models import TermsCondition


# Register your models here.
class Terms(admin.ModelAdmin):
    list_display = ('title_terms', 'description')


admin.site.register(TermsCondition, Terms)
