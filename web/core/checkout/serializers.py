from rest_framework import serializers
from .models import DeliveryOptions, PaymentSelections


class DeliveryOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryOptions
        fields = '__all__'


class PaymentSelectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSelections
        fields = '__all__'
