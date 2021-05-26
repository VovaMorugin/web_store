from django.core.exceptions import DisallowedHost
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField

# Create your models here.

class Brand(models.Model):
    class Meta:
        db_table = 'brands'
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    title = models.CharField(max_length=200)
    price = models.FloatField()
    old_price = models.FloatField()
    quantity = models.IntegerField()
    photo = models.ImageField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class ProductReview(models.Model):
    class Meta:
        db_table = 'product_reviews'
        verbose_name = 'product_review'
        verbose_name_plural = 'product_reviews'

    review = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    class Meta:
        db_table = 'product_categories'
        verbose_name = 'product_category'
        verbose_name_plural = 'product_categories'
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + self. category

class Promocode(models.Model):
    class Meta:
        db_table = 'promocodes'
        verbose_name = 'promocode'
        verbose_name_plural = 'promocodes'

    code = models.CharField(max_length=10)
    discount = models.FloatField()

    def __str__(self):
        return self.code

class Customer(models.Model):
    class Meta:
        db_table = 'customers'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    token = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class CustomerAddress(models.Model):
    class Meta:
        db_table = 'customer_addresses'
        verbose_name = 'customer_address'
        verbose_name_plural = 'customer_addresses'

    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.customer

class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    promocode = models.ForeignKey(Promocode, on_delete=CASCADE)
    customer_address = models.ForeignKey(CustomerAddress, on_delete=CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_checkout = models.DateTimeField()
    time_delivery = models.DateTimeField()

    def __str__(self):
        return self.customer + self.customer_address


class OrderProduct(models.Model):
    class Meta:
        db_table = 'order_products'
        verbose_name = 'order_product'
        verbose_name_plural = 'order_products'

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.order + self.product