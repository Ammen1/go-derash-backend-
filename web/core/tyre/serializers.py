from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from core.tyre.models import *
from core.account.serializers import CustomUserSerializer
from core.account.models import Car


from rest_framework import serializers


class TyreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TyreCategory
        fields = '__all__'


class TyreBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyreBrand
        fields = '__all__'


class TyreSerializer(serializers.ModelSerializer):
    category = TyreCategorySerializer()
    brand = TyreBrandSerializer()

    class Meta:
        model = Tyre
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = TyreSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
