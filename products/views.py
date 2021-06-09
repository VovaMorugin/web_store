from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, pagination, response
from .paginations import *
from .serializers import *
from .models import Category, Brand, Product, ProductCategory
from math import ceil

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

class ProductRetrive(generics.RetrieveAPIView):
    serializer_class = ProductRetriveSerializer
    queryset = Product.objects.all()


class ProductListFromCategory(generics.ListAPIView):
    serializer_class = ProductPreviewSerializer

    def get_queryset(self):
        product_ids = ProductCategory.objects.filter(
            category_id=self.kwargs['category_id']).values('product_id')
        return Product.objects.filter(pk__in=product_ids)


class ProductList(generics.ListAPIView):
    serializer_class = ProductPreviewSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination

class BrandRetrieve(generics.RetrieveAPIView):
    serializer_class = BrandRetriveWithPruductSerializer
    queryset = Brand.objects.all()
