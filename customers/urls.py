from django.urls import path
from .views import CustomerList, CustomerAddressesList

urlpatterns = [
    path('all/', CustomerList.as_view()),
    path('<int:customer_id>/', CustomerAddressesList.as_view())
]
