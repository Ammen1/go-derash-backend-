
from django.urls import path
from core.orders.views import AddToOrder, PaymentConfirmation, UserOrders

app_name = 'orders'


urlpatterns = [
    path('order/add/', AddToOrder.as_view(), name='add-to-order'),
    path('order/payment-confirmation/',
         PaymentConfirmation.as_view(), name='payment-confirmation'),
    path('user/orders/', UserOrders.as_view(), name='user-orders'),
]
