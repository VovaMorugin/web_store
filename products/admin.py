from django.contrib import admin
from .models import *
# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display = ['title']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'old_price', 'quantity', 'brand')

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'product')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'category')

class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Promocode, PromocodeAdmin)
