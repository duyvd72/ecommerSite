from django.contrib import admin
from .models import *

class MobilePhoneBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin',)

class DesignAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

class MobilePhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'width', 'import_price', 'design', 'mobile_phone_brand')


admin.site.register(Design, DesignAdmin)
admin.site.register(MobilePhoneBrand, MobilePhoneBrandAdmin)
admin.site.register(MobilePhone, MobilePhoneAdmin)



