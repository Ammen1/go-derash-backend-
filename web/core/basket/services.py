class BaseService:
    def __init__(self, service_type):
        self.service_type = service_type

    def calculate_total_cost(self):
        # Default implementation, can be overridden by specific service classes
        return 0  # You might want to adjust this default value based on your needs


class BatteryService(BaseService):
    def calculate_total_cost(self):
        battery = self.service_type.batteries.first()

        if battery:
            return battery.regular_price * battery.qty if battery.qty > 1 else battery.regular_price
        else:
            return 0


class EngineOilService(BaseService):
    def calculate_total_cost(self):
        total_engine_oil_price = sum(
            engine_oil.regular_price * engine_oil.qty for engine_oil in self.service_type.engine_oils.all())
        return total_engine_oil_price


class TyreService(BaseService):
    def calculate_total_cost(self):
        total_tyre_price = sum(
            tyre.regular_price * tyre.qty for tyre in self.service_type.tyres.all())
        return total_tyre_price


class CarWashService(BaseService):
    def calculate_total_cost(self):
        total_carwash_price = sum(
            carwash.regular_price * carwash.qty for carwash in self.service_type.carwashes.all())
        return total_carwash_price


class GasLineService(BaseService):
    def calculate_total_cost(self):
        total_gasline_price = sum(
            gasline.regular_price * gasline.qty for gasline in self.service_type.gaslines.all())
        return total_gasline_price
