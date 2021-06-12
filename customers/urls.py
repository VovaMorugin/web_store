from django.urls import path
from .views import CustomerList, CustomerAddressesList, customer_create

urlpatterns = [
    path('all/', CustomerList.as_view()),
    path('<int:customer_id>/', CustomerAddressesList.as_view()),
    path('create/', customer_create)
]
