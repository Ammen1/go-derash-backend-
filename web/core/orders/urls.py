from .views import OrderList, OrderDetail, OrderItemList, OrderItemDetail
from django.urls import path
from django.urls import path, include
from .views import *

app_name = 'orders'


urlpatterns = [
    path('orders/orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('order-items/', OrderItemList.as_view(), name='order-item-list'),
    path('order-items/<int:pk>/', OrderItemDetail.as_view(),
         name='order-item-detail'),
]
