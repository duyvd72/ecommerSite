from django.contrib import admin
from .models import *

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'phone','origin',)

class StyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'fabric', 'import_price', 'style', 'manufacturer')


admin.site.register(Style, StyleAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Clothes, ClothesAdmin)



