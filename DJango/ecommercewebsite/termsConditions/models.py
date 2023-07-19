from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class TermsCondition(models.Model):
    title_terms = models.CharField(max_length=200)
    description = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
