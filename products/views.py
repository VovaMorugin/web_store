from django.shortcuts import render
from rest_framework import generics
from . serializers import BrandSerializer, CategorySerializer, ProductSerializer
from .models import Category, Brand, Product
# Create your views here.

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class BrandList(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()