from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'old_price', 'quantity', 'brand']
    search_fields = ['title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'category']

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'review']