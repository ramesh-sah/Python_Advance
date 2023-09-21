from django.contrib import admin
from About.models import about



# Register your models here.
class AboutSection(admin.ModelAdmin):
    list_display = ['title', 'description','slug']

admin.site.register(about, AboutSection)

