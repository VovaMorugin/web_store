from django.urls import path
from .views import MyOrders, UserCreate, GetAuthCustomer, customer_create

urlpatterns = [
    path('create/', customer_create),
    path('registration/', UserCreate.as_view()),
    path('myorders/', MyOrders.as_view()),
    path('getuser/', GetAuthCustomer.as_view()),
]
