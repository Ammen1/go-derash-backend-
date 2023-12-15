from rest_framework import serializers
from core.base.models import *


class BaseServiceSerializer(serializers.Serializer):
    total_cost = serializers.DecimalField(max_digits=10, decimal_places=2)


class BatteryServiceSerializer(BaseServiceSerializer):
    battery_price = serializers.SerializerMethodField()

    class Meta:
        model = BaseService
        fields = ['total_cost', 'total_engine_oil_price']

    def get_battery_price(self, obj):
        battery = obj.batteries.first()

        if battery:
            total_battery_price = battery.regular_price * battery.qty
            return total_battery_price if battery.qty > 1 else battery.regular_price
        else:
            return None


class EngineOilServiceSerializer(BaseServiceSerializer):
    total_engine_oil_price = serializers.SerializerMethodField()

    class Meta:
        model = EngineOil
        fields = ['total_cost', 'total_engine_oil_price']

    def get_total_engine_oil_price(self, obj):
        engine_oils = obj.engine_oils.all()
        total_price = sum(
            engine_oil.regular_price * engine_oil.qty for engine_oil in engine_oils)
        return total_price


class TyreServiceSerializer(BaseServiceSerializer):
    total_tyre_price = serializers.SerializerMethodField()

    class Meta:
        model = Tyre
        fields = ['total_price', 'total_tyre_price']

    def get_total_tyre_price(self, obj):
        tyres = obj.tyres.all()
        total_price = sum(tyre.regular_price * tyre.qty for tyre in tyres)
        return total_price


class CarWashServiceSerializer(BaseServiceSerializer):
    total_carwash_price = serializers.SerializerMethodField()

    class Meta:
        model = CarWash
        fields = ['total_cost', 'total_carwash_price']

    def get_total_carwash_price(self, obj):
        carwashes = obj.carwashes.all()
        total_price = sum(
            carwash.regular_price * carwash.qty for carwash in carwashes)
        return total_price


class GasLineServiceSerializer(BaseServiceSerializer):
    total_gasline_price = serializers.SerializerMethodField()

    class Meta:
        model = ServiceType
        fields = ['total_cost', 'total_gasline_price']

    def get_total_gasline_price(self, obj):
        gaslines = obj.gaslines.all()
        total_price = sum(
            gasline.regular_price * gasline.qty for gasline in gaslines)
        return total_price
