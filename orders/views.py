from django.db.models.query import QuerySet
from orders.serializers import OrderProductSerializer, OrderSerializer
from django.shortcuts import HttpResponse
from .models import Order, OrderProduct
from rest_framework import generics, status
import json
from customers.models import Customer, CustomerAddress
from products.models import Product
from datetime import date, datetime
from rest_framework.response import Response

# /api/order/cart/update/
# update items in cart, must pass token, product_id and quantity, returns total number of items in the cart and status
# items in carts are stored in db so the user can continue shopping later.

def update_cart(request):
    if request.method == 'POST':
        try:
            request_json = json.loads(request.body)
            customer = Customer.objects.get(token=request_json['token'])
            product = Product.objects.get(pk=request_json['product_id'])
            orders = Order.objects.filter(customer=customer, is_ordered=False).order_by('-id')
            if orders.count() == 0:
                order = Order.objects.create(customer=customer)
            else:
                order = orders[0]

            try:
                product_order = OrderProduct.objects.get(product=product, order=order)
                if request_json['quantity'] == 0:
                    product_order.delete()
                else:
                    product_order.price = product.price
                    product_order.quantity = request_json['quantity']
                    product_order.save()
            except OrderProduct.DoesNotExist:
                OrderProduct.objects.create(
                    order=order,
                    product=product,
                    price=product.price,
                    quantity=request_json['quantity']
                )
            # cart = core_serializer.serialize('json', OrderProduct.objects.filter(order__customer__token=request_json['token']))
            count_products = OrderProduct.objects.filter(order__customer__token=request_json['token']).count()
            resp = {
                "status": True,
                "cart_items_count": count_products
            }
            return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK)
        except BaseException as e:
            resp = {
                "status": False,
                "error": str(e)
            }
            return HttpResponse(json.dumps(resp), status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# cart/list/<slug:customer_token>/
# return current item list from the cart, by user token

class CartList(generics.ListAPIView):
    serializer_class = OrderProductSerializer
    queryset = OrderProduct

    def get_queryset(self):
        try:
            return OrderProduct.objects.filter(
                order__customer__token=self.kwargs['customer_token'],
                order__is_ordered=False
            )
        except BaseException:
            return None


# /api/order/finalize/
# Finilizes order, accept token, first_name, last_name, email, country, city, post_code and address. And automatically takes the products in users cart,


class OrderFinalize(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order

    def update(self, request, *args, **kwargs):
        try:
            request_json = request.data
            customer = Customer.objects.get(token=request_json['token'])
            instance = Order.objects.filter(customer=customer, is_ordered=False).order_by('-id')[0]
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            customer.first_name = request_json['first_name']
            customer.last_name = request_json['last_name']
            customer.email = request_json['email']


            address = CustomerAddress.objects.create(
                customer = customer,
                country = request_json['country'],
                city = request_json['city'],
                post_code = request_json['post_code'],
                address = request_json['address'],
            )

            instance.customer_shipping_address = address
            instance.is_ordered = True
            instance.time_checkout = datetime.now()

            customer.save()
            instance.save()

            return Response(serializer.data)
        except BaseException as err:
            return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)