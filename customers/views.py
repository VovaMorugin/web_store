from .serializers import CustomerAddressSerializer, CustomerSerializer
from django.shortcuts import render, HttpResponse
from rest_framework import generics, permissions
from .models import Customer, CustomerAddress
import uuid
import json

# Create your views here.


class CustomerList(generics.ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [permissions.IsAdminUser]


class CustomerAddressesList(generics.ListAPIView):
    serializer_class = CustomerAddressSerializer

    def get_queryset(self):
        return CustomerAddress.objects.filter(customer_id=self.kwargs['customer_id'])


def customer_create(request):
    if request.method == 'POST':
        try:
            customer_token = str(uuid.uuid4())
            Customer.objects.create(token=customer_token)
            response = {
                'status': True,
                'customer_token': customer_token
            }
        except BaseException:
            response = {
                'status': False,
            }
    else:
        response = {
            'status': False,
            'message': 'Else'
        }
    return HttpResponse(json.dumps(response))
