from .serializers import CustomerSerializer, UserSerializer, MyOrdersSerializer
from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import generics
from .models import Customer
from orders.models import Order
import uuid
import json
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
User = get_user_model()

# /api/customer/create/
# When the user opens the store for the first time we can call this method to create new customer model and return unique customer token 
# All properties except Token could be null, which allows us to start using this model right away, without additional information.

def customer_create(request):
    if request.method == 'POST':
        try:
            customer_token = str(uuid.uuid4())
            Customer.objects.create(token=customer_token)
            response = {
                "status": True,
                "customer_token": customer_token
            }
        except BaseException:
            response = {
                "status": False,
            }
    else:
        response = {
            "status": False
        }
    return HttpResponse(json.dumps(response))

# /api/customer/registration/
# When you create a user this method will use customer token to bind user with customer 
# You have to pass User_name, "password", "email", "first_name", "last_name" and "token"

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User


# /api/customer/myorders/
# Return all orders binded to current user


class MyOrders(generics.ListAPIView):
    serializer_class = MyOrdersSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Order.objects.filter(customer__user=self.request.user)


# /api/customer/getuser/
# Return authed current customer

class GetAuthCustomer(generics.RetrieveAPIView):
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        customer = get_object_or_404(Customer, user=self.request.user)
        return customer
