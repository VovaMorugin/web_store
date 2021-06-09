from .serializers import CustomerAddressSerializer, CustomerSerializer
from django.shortcuts import render
from rest_framework import generics
from .models import Customer, CustomerAddress
# Create your views here.

class CustomerList(generics.ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class CustomerAddressesList(generics.ListAPIView):
    serializer_class = CustomerAddressSerializer
    def get_queryset(self):
        return CustomerAddress.objects.filter(customer_id = self.kwargs['customer_id'])