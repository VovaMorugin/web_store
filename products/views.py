from django.shortcuts import render
from rest_framework import generics
from . serializers import BrandSerializer, CategorySerializer, ProductSerializer
from .models import Category, Brand, Product
# Create your views here.

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    def get_queryset(self):
        return Category.objects.filter(is_active = True)

class BrandList(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer

class CategoryRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()