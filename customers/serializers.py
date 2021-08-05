from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Customer
from orders.models import Order, OrderProduct

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            try:
                customer = Customer.objects.get(
                    token=self.context['request'].data['token'])
                customer.user = user
                customer.first_name = validated_data['first_name']
                customer.last_name = validated_data['last_name']
                customer.first_name = validated_data['email']
                customer.save()
            except BaseException as e:
                print(e)
            user.set_password(validated_data['password'])
            user.save()

            return user
        except BaseException:
            return False


class ProductField(serializers.RelatedField):
    def to_representation(self, value):
        return value.title


class MyOrderProductSerializer(serializers.ModelSerializer):
    product = ProductField(many=False, read_only=True)

    class Meta:
        model = OrderProduct
        fields = ['order_id', 'product_id', 'price', 'quantity', 'product']


class MyOrdersSerializer(serializers.ModelSerializer):
    products = MyOrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'is_ordered', 'time_created',
                  'time_checkout', 'time_delivery', 'products']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
