from django.db.models.query import QuerySet
from orders.serializers import OrderProductSerializer, OrderSerializer
from django.shortcuts import HttpResponse
from .models import Order, OrderProduct
from rest_framework import generics, status
import json
from customers.models import Customer
from products.models import Product

# Create your views here.


class OrdersList(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderProductsList(generics.ListAPIView):
    serializer_class = OrderProductSerializer

    def get_queryset(self):
        return OrderProduct.objects.filter(order_id=self.kwargs['order_id'])


def update_cart(request):
    if request.method == 'POST':
        try:
            request_json = json.loads(request.body)
            print(request_json)

            customer = Customer.objects.get(token=request_json['token'])
            product = Product.objects.get(pk=request_json['product_id'])

            try:
                order = Order.objects.get(customer=customer)
            except Order.DoesNotExist:
                order = Order.objects.create(customer=customer)

            # orders = Order.objects.filter(customer=customer)

            # if orders.count() == 0:
            #     Order.objects.create(customer=customer)
            # else:
            #     order = orders[0]

            try:
                product_order = OrderProduct.objects.get(
                    product=product, order=order)
                if request_json['quantity'] == 0:
                    product_order.delete()
                else:
                    product_order.price = product.price
                    product_order.quantity = request_json['quantity']
                    product_order.save()
            except OrderProduct.DoesNotExist:
                if request_json['quantity'] > 0:
                    product_order = OrderProduct.objects.create(
                        order=order,
                        product=product,
                        price=product.price,
                        quantity=request_json['quantity'],
                    )

            count_products = OrderProduct.objects.filter(order=order).count()

            res = {
                'status': True,
                'cart_items_count': count_products
            }
            return HttpResponse(json.dumps(res))
        except BaseException as e:
            res = {
                'status': False,
                'error': str(e)
            }
            return HttpResponse(json.dumps(res), status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class CartList(generics.ListAPIView):
    serializer_class = OrderProductSerializer 
    def get_queryset(self):
        try:
            return OrderProduct.objects.filter(order__customer__token = self.kwargs['customer_token'])
        except BaseException:
            return None