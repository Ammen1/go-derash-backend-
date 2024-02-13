from django.urls import path
from django.urls import path, include
from . views import *


app_name = 'basket'


urlpatterns = [

    path('update/', BasketUpdate.as_view(), name='basket_update'),
    path('basket/add/', BasketAdd.as_view(), name='basket-add'),
    path('basket/delete/',
         BasketDelete.as_view(), name='basket-delete'),

]
