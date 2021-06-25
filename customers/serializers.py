from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Customer, CustomerAddress
from orders.models import Order, OrderProduct

User = get_user_model()


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        try:
            user = User.obrects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name', ]
            )
            try:
                customer = Customer.objects.get(
                    token=self.context['request'].data['token'])
                customer.user = user
                if len(customer.first_name) == 0:
                    customer.first_name = validated_data['first_name']
                if len(customer.last_name) == 0:
                    customer.last_name = validated_data['last_name']
                if len(customer.email) == 0:
                    customer.email = validated_data['email']
                customer.save()

            except BaseException as er:
                pass
            user.set_password(validated_data['password'])
            user.save()
            return user
        except BaseException as e:
            return False

class ProductField(serializers.RelatedField):
    def to_representation(self, value):
        return value.title

class MyOrderProductSerializer(serializers.ModelSerializer):
    product = ProductField(many=False, read_only=True)
    class Meta:
        model = OrderProduct
        fields = ['order_id', 'product_id', 'price', 'quantity', 'product']
        # fields = '__all__'

class MyOrdersSerializer(serializers.ModelSerializer):
    products = MyOrderProductSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'is_ordered', 'time_created', 'time_checkout', 'time_delivery', 'products']



    #         customer = models.ForeignKey(Customer, on_delete=CASCADE, null=False, blank=False, verbose_name='Customer')
    # promocode = models.ForeignKey(Promocode, on_delete=CASCADE, null=True, blank=True)
    # customer_shipping_address = models.ForeignKey(CustomerAddress, on_delete=CASCADE, null=True, blank=True, verbose_name='Shipping address')
    # time_created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    # time_checkout = models.DateTimeField(null=True, blank=True, verbose_name='Time of checkout')
    # time_delivery = models.DateTimeField(null=True, blank=True, verbose_name='Time of delivery')
    # is_ordered = models.BooleanField(default=False, verbose_name='Is ordered')