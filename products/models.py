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

    title = models.CharField(null=False, blank=False, max_length=200, verbose_name='Title')

    def __str__(self):
        return self.title


class Product(models.Model):
    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    title = models.CharField(null=False, blank=False, max_length=200, verbose_name='Title')
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False, default=0, verbose_name='Price')
    old_price = models.FloatField(null=True, blank=True, default=0, verbose_name='Old price')
    quantity = models.IntegerField(default=1, null=False, blank=False, verbose_name='Quantity')
    photo = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Photo')
    brand = models.ForeignKey(Brand, related_name='product', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Brand')
    description = models.TextField()

    def __str__(self):
        return str(self.title)



class ProductReview(models.Model):
    class Meta:
        db_table = 'product_reviews'
        verbose_name = 'product_review'
        verbose_name_plural = 'product_reviews'

    review = models.TextField(null=False, blank=False,verbose_name='Review')
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Product')

class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    title = models.CharField(max_length=200)
    is_active = models.BooleanField(null=False, blank=False, default=True, verbose_name='Active')
    
    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    class Meta:
        db_table = 'product_categories'
        verbose_name = 'product_category'
        verbose_name_plural = 'product_categories'
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Category')

    def __str__(self):
        return str(self.category)

class Promocode(models.Model):
    class Meta:
        db_table = 'promocodes'
        verbose_name = 'promocode'
        verbose_name_plural = 'promocodes'

    code = models.CharField(max_length=10)
    discount = models.FloatField()

    def __str__(self):
        return self.code





