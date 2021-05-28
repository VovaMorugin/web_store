from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']

@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'country', 'city', 'post_code', 'address']