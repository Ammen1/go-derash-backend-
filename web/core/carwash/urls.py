from django.urls import path, include
from .views import *

app_name = 'carwash'

urlpatterns = [
    path('user/carwashorder/', CarWashOrderCreateView.as_view(), name='carwashorder'),
    path('user/carwasall/', CarWashOrderListView.as_view(), name='carwashall'),
    path('user/detailcarwash/<int:pk>/',
         DetailCarWash.as_view(), name='detailcarwash'),
    path('user/detelecarwash/<int:pk>/',
         DeleteCarWash.as_view(), name='detelecarwash'),
    path('user/editcarwash/<int:pk>/', EditCarWash.as_view(), name='editcarwash'),
]
