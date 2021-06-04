from rest_framework import serializers
from .models import Category, Brand, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'is_active']

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
