from django.contrib import admin
from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name',)

class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

class CustomerAdmin(admin.ModelAdmin):
    list_display=("idCard",'mail')

class VariationAdmin(admin.ModelAdmin):
    list_display = ('item', 'variation_category', 'variation_value', 'is_active',)
    list_editable = ('is_active',)
    list_filter = ('item', 'variation_category', 'variation_value', 'is_active',)


class LaptopItemAdmin(admin.ModelAdmin):
    list_display = ('laptop', 'public_price', 'version', 'cpu', 'ram', 'color', 'is_available')
    prepopulated_fields = {'slug': ('item_name',)}


class ClothesItemAdmin(admin.ModelAdmin):
    list_display = ('clothes', 'public_price', 'size', 'color', 'is_available')
    prepopulated_fields = {'slug': ('item_name',)}


class MobilePhoneItemAdmin(admin.ModelAdmin):
    list_display = ('mobile_phone', 'public_price', 'chip', 'ram', 'color', 'is_available')
    prepopulated_fields = {'slug': ('item_name',)}


admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(LaptopItem, LaptopItemAdmin)
admin.site.register(ClothesItem, ClothesItemAdmin)
admin.site.register(MobilePhoneItem, MobilePhoneItemAdmin)
admin.site.register(Item, ItemAdmin)
