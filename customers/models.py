from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Customer(models.Model):
    class Meta:
        db_table = 'customers'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    token = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='First name')
    last_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Last name')
    phone = models.BigIntegerField(null=True, blank=True, verbose_name='Phone')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='Email')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Created')

    def __str__(self):
        return self.first_name


class CustomerAddress(models.Model):
    class Meta:
        db_table = 'customer_addresses'
        verbose_name = 'customer_address'
        verbose_name_plural = 'customer_addresses'

    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    country = models.CharField(max_length=200, null=False, blank=False, verbose_name='Country')
    city = models.CharField(max_length=200, null=False, blank=False, verbose_name='City')
    post_code = models.IntegerField(null=False, blank=False, verbose_name='Post code')
    address = models.CharField(max_length=200, null=False, blank=False, verbose_name='Address')

    def __str__(self):
        return self.customer