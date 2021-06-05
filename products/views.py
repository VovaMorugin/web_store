from django.shortcuts import render
from rest_framework import generics
from . serializers import BrandSerializer, CategorySerializer, ProductSerializer, CategoryRetriveSerializer, CategoryListSerializer
from .models import Category, Brand, Product
# Create your views here.


class CategoryList(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        return Category.objects.filter(is_active=True)


class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer
    

class CategoryRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryRetriveSerializer
    queryset = Category.objects.all()


class CategoryRetrive(generics.RetrieveAPIView):
    serializer_class = CategoryRetriveSerializer
    queryset = Category.objects.all()

class BrandList(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

class BrandRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
