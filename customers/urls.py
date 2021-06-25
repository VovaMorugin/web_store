from django.urls import path
from .views import CustomerList, CustomerAddressesList, MyOrders, UserCreate, customer_create, GetAuthCustomer

urlpatterns = [
    path('all/', CustomerList.as_view()),
    path('<int:customer_id>/', CustomerAddressesList.as_view()),
    path('create/', customer_create),
    path('registration/', UserCreate.as_view()),
    path('myorders/', MyOrders.as_view()),
    path('getuser/', GetAuthCustomer.as_view())
]
