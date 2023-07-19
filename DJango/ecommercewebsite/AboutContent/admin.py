from django.contrib import admin
from AboutContent.models import AboutPageContent


# Register your models here.
class AboutPage(admin.ModelAdmin):
    list_display = ('about_page_title', 'about_page_description')


admin.site.register(AboutPageContent, AboutPage)
