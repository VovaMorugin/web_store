from products.models import Product
from django.urls import path
from .views import BrandRUD, CategoryCreate, CategoryList, BrandList, CategoryRUD, CategoryRetrive, ProductList


urlpatterns = [
    path('category/list/', CategoryList.as_view()),
    path('brand/list/', BrandList.as_view()),
    path('list/', ProductList.as_view()),
    path('category/add/', CategoryCreate.as_view()),
    path('category/<int:pk>/', CategoryRUD.as_view()),
    path('category/get/<int:pk>/', CategoryRetrive.as_view()),
    path('brand/<int:pk>/', BrandRUD.as_view())
]