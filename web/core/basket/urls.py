from .views import (
    BaseServiceView, BatteryServiceView, EngineOilServiceView,
    TyreServiceView, CarWashServiceView, GasLineServiceView
)
from django.urls import path
from django.urls import path, include


app_name = 'basket'


urlpatterns = [
    path('services/base/<int:pk>/',
         BaseServiceView.as_view(), name='base-service'),
    path('service/battery/<int:pk>/',
         BatteryServiceView.as_view(), name='battery-service'),
    path('service/engine-oil/<int:pk>/',
         EngineOilServiceView.as_view(), name='engine-oil-service'),
    path('services/tyre/<int:pk>/',
         TyreServiceView.as_view(), name='tyre-service'),
    path('services/car-wash/<int:pk>/',
         CarWashServiceView.as_view(), name='car-wash-service'),
    path('services/gas-line/<int:pk>/',
         GasLineServiceView.as_view(), name='gas-line-service'),
]
