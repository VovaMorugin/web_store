from django.db import models
from customers.models import Customer, CustomerAddress
from products.models import Promocode, Product
from django.db.models.deletion import CASCADE
# Create your models here.

class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    customer = models.ForeignKey(Customer, on_delete=CASCADE, null=False, blank=False, verbose_name='Customer')
    promocode = models.ForeignKey(Promocode, on_delete=CASCADE)
    customer_shipping_address = models.ForeignKey(CustomerAddress, on_delete=CASCADE, null=True, blank=True, verbose_name='Shipping address')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    time_checkout = models.DateTimeField(null=True, blank=True, verbose_name='Time of checkout')
    time_delivery = models.DateTimeField(null=True, blank=True, verbose_name='Time of delivery')

    def __str__(self):
        return self.customer + self.customer_address


class OrderProduct(models.Model):
    class Meta:
        db_table = 'order_products'
        verbose_name = 'order_product'
        verbose_name_plural = 'order_products'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Product')
    quantity = models.IntegerField(default=1, null=False, blank=False, verbose_name='Quantity')
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False, default=0, verbose_name='Price')

    def __str__(self):
        return self.order + self.product