from django.db import models


class AutoCostCalculator(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    distance_travelled = models.DecimalField(max_digits=8, decimal_places=2)
    service_used = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_type_used = models.ForeignKey(
        ServiceType, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
