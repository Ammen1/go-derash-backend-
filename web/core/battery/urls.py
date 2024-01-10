from django.urls import path, include
from .views import *

app_name = 'battery'

urlpatterns = [
    path('user/batteryorder/', BatteryOrderView.as_view(), name='batteryorder'),

]
