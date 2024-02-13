from core.checkout.views import (
    PaymentConfirmation, PaymentComplete, Basket_Update_Delivery
)
from django.urls import path

from .views import *
from . import views

app_name = 'checkout'


urlpatterns = [
    path('order/payment-confirmation/',
         PaymentConfirmation.as_view(), name='payment-confirmation'),
    path("basket_update_delivery/", Basket_Update_Delivery.as_view(),
         name="basket_update_delivery"),
    path('order/payment-complete/',
         PaymentComplete.as_view(), name='payment-complete'),


]
