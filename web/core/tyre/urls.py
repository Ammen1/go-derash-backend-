from django.urls import path, include
from .views import *

app_name = 'tyre'

urlpatterns = [
    path('tyres/all/', TyreAllAPIView.as_view(), name='tyre-all'),
    path('tyres/category/<str:category_slug>/',
         TyreCategoryListAPIView.as_view(), name='tyre-category-list'),
    path('tyres/detail/<str:slug>/',
         TyreDetailAPIView.as_view(), name='tyre-detail'),

    path('order/add/', AddToOrderView.as_view(), name='add-to-order'),
    path('order/payment-confirmation/',
         PaymentConfirmationView.as_view(), name='payment-confirmation'),
    path('user/orders/', UserOrdersView.as_view(), name='user-orders'),


]
