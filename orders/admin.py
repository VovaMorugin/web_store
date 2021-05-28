from django.contrib import admin
from .models import *
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'promocode', 'customer_shipping_address')


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)