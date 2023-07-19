from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class refund(models.Model):
    title_refund = models.CharField(max_length=225)
    description = HTMLField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
