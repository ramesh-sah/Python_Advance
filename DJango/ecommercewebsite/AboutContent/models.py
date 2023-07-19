from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class AboutPageContent(models.Model):
    about_page_title = models.CharField(max_length=50)
    about_page_description = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
