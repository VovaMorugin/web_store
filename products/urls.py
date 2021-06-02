from products.models import Product
from django.urls import path
from .views import CategoryList, BrandList, ProductList


urlpatterns = [
    path('category/list/', CategoryList.as_view()),
    path('brand/list/', BrandList.as_view()),
    path('product/list/', ProductList.as_view())
]