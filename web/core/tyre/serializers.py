from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from core.tyre.models import *
from core.account.serializers import CustomUserSerializer


class TyreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TyreCategory
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyreBrand
        fields = '__all__'


class TyreSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
    car_type = serializers.CharField(write_only=True)
    brand = serializers.CharField(write_only=True)

    class Meta:
        model = Tyre
        fields = '__all__'

    def get_total_cost(self, obj):
        total_price = obj.total_price()
        total_cost = total_price * obj.qty

        return total_cost

    def to_internal_value(self, data):
        if 'car_type' in data and isinstance(data['car_type'], str):
            vehicle_info = VehicleInformation.objects.filter(
                vehicle_type=data['car_type']).first()
            if vehicle_info:
                data['car_type'] = vehicle_info.pk

    def to_internal_value(self, data):
        if 'brand' in data and isinstance(data['brand'], str):
            brand = TyreBrand.objects.filter(name=data['brand']).first()

            if brand:
                data['brand'] = brand.pk
        return super().to_internal_value(data)


# class OrderItemSerializer(serializers.ModelSerializer):
#     fuel = TyreSerializer()

#     class Meta:
#         model = OrderItem
#         fields = ['id', 'tyre', 'price', 'quantity']


# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True, read_only=True)

#     class Meta:
#         model = Order
#         fields = ['id', 'user', 'full_name', 'email', 'address', 'city',
#                   'phone', 'created', 'updated', 'total_paid',
#                   'order_key', 'payment_option', 'billing_status', 'items']

#     def create(self, validated_data):
#         items_data = validated_data.pop('items')
#         order = Order.objects.create(**validated_data)
#         for item_data in items_data:
#             fuel_data = item_data.pop('fuel')
#             fuel = Fuel.objects.create(**fuel_data)
#             OrderItem.objects.create(order=order, fuel=fuel, **item_data)
#         return order
