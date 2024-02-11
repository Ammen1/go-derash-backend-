from .views import (
    DeliveryOptionsListCreateView,
    DeliveryOptionsRetrieveUpdateDestroyView,
    PaymentSelectionsListCreateView,
    PaymentSelectionsRetrieveUpdateDestroyView,
)
from django.urls import path

from .views import *
from . import views

app_name = 'checkout'


urlpatterns = [
    path('delivery-options/', DeliveryOptionsListCreateView.as_view(),
         name='delivery-options-list-create'),
    path('delivery-options/<int:pk>/',
         DeliveryOptionsRetrieveUpdateDestroyView.as_view(), name='delivery-options-detail'),

    path('payment-selections/', PaymentSelectionsListCreateView.as_view(),
         name='payment-selections-list-create'),
    path('payment-selections/<int:pk>/',
         PaymentSelectionsRetrieveUpdateDestroyView.as_view(), name='payment-selections-detail'),
    path("basket_update_delivery/", views.basket_update_delivery,
         name="basket_update_delivery"),

]
