from orders.serializers import OrderProductSerializer, OrderSerializer
from django.shortcuts import render
from .models import Order, OrderProduct
from rest_framework import generics

# Create your views here.
class OrdersList(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderProductsList(generics.ListAPIView):
    serializer_class = OrderProductSerializer
    def get_queryset(self):
        return OrderProduct.objects.filter(order_id = self.kwargs['order_id'])