from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']

class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'country', 'city', 'post_code', 'address']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerAddress, CustomerAddressAdmin)