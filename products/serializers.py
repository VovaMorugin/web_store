from rest_framework import serializers
from .models import Category, Brand, Product, ProductReview

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'is_active']

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class BrandField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'id': value.id,
            'title': value.title
        }

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['product', 'review']

class ProductRetriveSerializer(serializers.ModelSerializer):
    reviews = ProductReviewSerializer(many=True, read_only=True)
    brand = BrandField(many = False, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'old_price', 'quantity', 'photo', 'brand', 'description', 'reviews']

class ProductPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'old_price', 'photo']

class BrandRetriveWithPruductSerializer(serializers.ModelSerializer):
    product = ProductRetriveSerializer(many=True, read_only=True)
    class Meta:
        model = Brand
        fields = ['id', 'title', 'product']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title']