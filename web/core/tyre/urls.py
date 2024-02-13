from django.urls import path, include
from .views import *
from . import views


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
    path('order/payment-complete/',
         PaymentCompleteView.as_view(), name='payment-complete'),
     path("basket_update_delivery/", Basket_Update_Delivery.as_view(),
          name="basket_update_delivery"),
    path('update/', BasketUpdate.as_view(), name='basket_update'),
    path('basket/add/', BasketAddView.as_view(), name='basket-add'),
    path('basket/delete/',
         BasketDeleteView.as_view(), name='basket-delete'),


]
