from django.contrib import admin

from customer.models import *
admin.site.register(Customer)
admin.site.register(Fullname)
admin.site.register(customerMember)
admin.site.register(Address)
admin.site.register(Account)
admin.site.register(Comment)