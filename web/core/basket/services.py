# services.py

class BaseService:
    def __init__(self, service_type):
        self.service_type = service_type

    def calculate_total_cost(self):
        # Default implementation, can be overridden by specific service classes
        return self.service_type.regular_price


class BatteryService(BaseService):
    def calculate_total_cost(self):
        # Custom implementation for Battery service
        battery_price = self.service_type.batteries.first().regular_price
        return battery_price


class EngineOilService(BaseService):
    def calculate_total_cost(self):
        # Custom implementation for Engine Oil service
        total_engine_oil_price = sum(
            engine_oil.regular_price for engine_oil in self.service_type.engine_oils.all())
        return total_engine_oil_price
