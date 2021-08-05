from django.db.models.query import QuerySet
from rest_framework import generics, filters
from .paginations import ProductPagination
from .serializers import *
from .models import Category, Brand, Product, ProductCategory
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *

# /api/product/category/list/
# return all product categories
class CategoryList(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()
    def get_queryset(self):
        return Category.objects.filter(is_active=True)


# /api/product/category/get/<int:pk>/
# return product category by id
class CategoryRetrieve(generics.RetrieveAPIView):
    serializer_class = CategoryRetrieveSerializer
    queryset = Category.objects.all()

# /api/product/get/<int:pk>/
# return product info by id
class ProductRetrieve(generics.RetrieveAPIView):
    serializer_class = ProductRetrieveSerializer
    queryset = Product.objects.all()


# /category/<int:category_id>/products/
# return product by category / query_set filter could be applied
class ProductListFromCategory(generics.ListAPIView):
    serializer_class = ProductPreviewSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'brand__title']
    ordering_fields = ['title', 'price']

    def get_queryset(self):
        product_ids = ProductCategory.objects.filter(category_id=self.kwargs['category_id']).values('product_id')
        return Product.objects.filter(pk__in=product_ids)
        # SELECT * FROM products WHERE id in (1,2,3,4,5)

# /api/product/all/
# return all products pagination and filters could be applied

class ProductList(generics.ListAPIView):
    serializer_class = ProductPreviewSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'brand__title']
    ordering_fields = ['title', 'price']

# /api/product/brands/all/
# return all brand list
class BrandRetrieve(generics.RetrieveAPIView):
    serializer_class = BrandRetrieveWithProductSerializer
    queryset = Brand.objects.all()

# /api/product/brands/get/<int:pk>/
# return spercific brand by id
class BrandList(generics.ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()