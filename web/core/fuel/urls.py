from django.urls import path, include
from .views import *

app_name = 'fuel'

urlpatterns = [
    # CarWah URLS
    path('user/orderfuel/', FuelOrderCreateView.as_view(), name='orderfuel'),
    path('user/allfuel/', ListFuel.as_view(), name='allfuel'),
    path('user/detailfuel/<int:pk>/', DetailGasline.as_view(), name='detailfuel'),
    path('user/detelefuel/', DeleteGasline.as_view(), name='detelefuel'),
    path('user/editfuel/', UpdateGasline.as_view(), name='editfuel'),

]
