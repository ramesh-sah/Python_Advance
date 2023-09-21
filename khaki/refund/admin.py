from django.contrib import admin
from refund.models import Refund
# Register your models here.
class RefundPolicy(admin.ModelAdmin):
    list_display=['title','description','slug']

admin.site.register(Refund,RefundPolicy)
