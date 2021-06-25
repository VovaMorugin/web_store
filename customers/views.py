from .serializers import CustomerAddressSerializer, CustomerSerializer, UserSerializer, MyOrdersSerializer
from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import generics, permissions
from .models import Customer, CustomerAddress
from orders.models import Order
import uuid
import json
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
User = get_user_model()
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


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User

class MyOrders(generics.ListAPIView):
    serializer_class = MyOrdersSerializer
    authentication_clasees = [JWTAuthentication,]
    permission_classes =[IsAuthenticated,]
    def get_queryset(self):
        return Order.objects.filter(customer__user=self.request.user)
    
class GetAuthCustomer(generics.RetrieveAPIView):
    serializer_class = CustomerSerializer
    authentication_clasees = [JWTAuthentication,]
    permission_classes =[IsAuthenticated,]
    def get_object(self):
        customer = get_object_or_404(Customer, user = self.request.user)
        return customer