from django.contrib import admin
from .models import *

class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin',)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'import_price', 'type', 'producer')

class LaptopItemAdmin(admin.ModelAdmin):
    list_display = ('laptop', 'slug', 'public_price', 'version', 'cpu', 'ram', 'color', 'is_available')


admin.site.register(Type, TypeAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(LaptopItem, LaptopItemAdmin)


