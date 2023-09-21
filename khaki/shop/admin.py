from django.contrib import admin
from shop.models import MensCloths,MensShoes,MensWatches,WomensHandbags,WomensGlasses
# Register your models here.
class MenCloth(admin.ModelAdmin):
    list_display = ['product_image',
                    'product_category',
                    'product_name',
                    'product_price',
                    'product_short_description',
                    'product_long_description',
                    'product_quantity',
                    'slug'
                   ]

admin.site.register(MensCloths,MenCloth)

class MenShoes(admin.ModelAdmin):
    list_display = ['product_image',
                    'product_category',
                    'product_name',
                    'product_price',
                    'product_short_description',
                    'product_long_description',
                    'product_quantity',
                    'slug'
                   ]

admin.site.register(MensShoes,MenShoes)


class MenWatches(admin.ModelAdmin):
    list_display = ['product_image',
                    'product_category',
                    'product_name',
                    'product_price',
                    'product_short_description',
                    'product_long_description',
                    'product_quantity',
                    'slug'
                   ]

admin.site.register(MensWatches,MenWatches)

class WomenHandbags(admin.ModelAdmin):
    list_display = ['product_image',
                    'product_category',
                    'product_name',
                    'product_price',
                    'product_short_description',
                    'product_long_description',
                    'product_quantity',
                    'slug'
                   ]

admin.site.register(WomensHandbags,WomenHandbags)

class WomenGlasses(admin.ModelAdmin):
    list_display = ['product_image',
                    'product_category',
                    'product_name',
                    'product_price',
                    'product_short_description',
                    'product_long_description',
                    'product_quantity',
                    'slug'
                   ]

admin.site.register(WomensGlasses,WomenGlasses)





