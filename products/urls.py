from products.models import Product
from django.urls import path
from .views import CategoryCreate, CategoryList, BrandList, CategoryRUD, ProductList


urlpatterns = [
    path('category/list/', CategoryList.as_view()),
    path('brand/list/', BrandList.as_view()),
    path('product/list/', ProductList.as_view()),
    path('category/add/', CategoryCreate.as_view()),
    path('category/<int:pk>/', CategoryRUD.as_view())
]