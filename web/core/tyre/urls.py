from django.urls import path, include
from .views import *

app_name = 'tyre'

urlpatterns = [
    # Tyre URLs
    path('user/tyre/create/', CreateTyre.as_view(), name='create'),
    path('user/tyre/list/', ListTyre.as_view(), name='list_tyre'),
    path('user/tyre/detail/<int:pk>/', DetailTyre.as_view(), name='detail_tyre'),
    path('user/tyre/delete/<int:pk>/', DeleteTyre.as_view(), name='delete_tyre'),
    path('user/tyre/edit/<int:pk>/', UpdateTyre.as_view(), name='edit_tyre'),
    # TyreCategory URLs
    path('user/tyre/createtyrecategory/',
         CreateTyreCategory.as_view(), name='createtyrecategory'),
    path('user/tyre/listtyrecategory/',
         ListTyreCategory.as_view(), name='listtyrecategory'),
    path('user/tyre/detailtyrecategory/<int:pk>/',
         DetailTyreCategory.as_view(), name='detailtyrecategory'),
    path('user/tyre/deletetyrecategory/<int:pk>/',
         DeleteTyreCategory.as_view(), name='deletetyrecategory'),
    path('user/tyre/edittyrecategory/<int:pk>/',
         UpdateTyreCategory.as_view(), name='edittyrecategory'),
    # TyreBrand URLs
    path('user/tyre/createtyrebrand/',
         CreateTyreBrand.as_view(), name='createtyrebrand'),
    path('user/tyre/listtyrebrand/',
         ListTyreBrand.as_view(), name='listtyrebrand'),
    path('user/tyre/detailtyrebrand/<int:pk>/',
         DetailTyreBrand.as_view(), name='detailtyrebrand'),
    path('user/tyre/deletetyrebrand/<int:pk>/',
         DeleteTyreBrand.as_view(), name='deletetyrebrand'),
    path('user/tyre/edittyrebrand/<int:pk>/',
         UpdateTyreBrand.as_view(), name='edittyrebrand'),

    # Order URLs
    #     path('user/tyre/createOrder/',
    #          CreateOrder.as_view(), name='createOrder'),
    #     path('user/tyre/listOrder/',
    #          ListOrder.as_view(), name='listOrder'),
    #     path('user/tyre/detailOrder/<int:pk>/',
    #          DetailOrder.as_view(), name='detailOrder'),
    #     path('user/tyre/deleteOrder/<int:pk>/',
    #          DeleteOrder.as_view(), name='deleteOrder'),
    #     path('user/tyre/editOrder/<int:pk>/',
    #          UpdateOrder.as_view(), name='editOrder'),
]
