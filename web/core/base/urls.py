# your_app/urls.py

from django.urls import path, include
from .views import *

app_name = 'base'

urlpatterns = [
    # Admin URLs
    path('admin/createcategory/', CreateCategory.as_view(), name='createcategory'),
    path('admin/listcategory/', CategoryList.as_view(), name='listcategory'),
    path('admin/detailcategory/<int:pk>/',
         CategoryDetail.as_view(), name='detailcategory'),
    path('admin/editcategory/<int:pk>/',
         EditCategory.as_view(), name='editcategory'),
    path('admin/deletecategory/<int:pk>/',
         DeleteCategory.as_view(), name='deletecategory'),

    # Vehicle Information URLs
    path('admin/listvehicleinformation/',
         ListVehicleInformation.as_view(), name='listvehicleinformation'),
    path('admin/deletevehicleinformation/<int:pk>/',
         DeleteVehicleInformation.as_view(), name='deletevehicleinformation'),

    # Tyre URLs
    path('admin/tyre/create/', CreateTyre.as_view(), name='create'),
    path('admin/tyre/list/', ListTyre.as_view(), name='list_tyre'),
    path('admin/tyre/detail/<int:pk>/', DetailTyre.as_view(), name='detail_tyre'),
    path('admin/tyre/delete/<int:pk>/', DeleteTyre.as_view(), name='delete_tyre'),
    path('admin/tyre/edit/<int:pk>/', EditTyre.as_view(), name='edit_tyre'),

    # CarWah URLS
    path('user/orderfuel/', FuelOrderCreateView.as_view(), name='orderfuel'),

    # Subscriptions URLS
    path('admin/listsubscriptions/',
         ListSubscriptions.as_view(), name='listsubscriptions'),
    path('admin/deletesubscription/<int:pk>/',
         DeleteSubscription.as_view(), name='deletesubscription'),



    # User URLs
    path('user/createvehicleinformation/',
         CreateVehicleInformation.as_view(), name='createvehicleInformation'),
    path('user/editvehicleinformation/<int:pk>/',
         EditVehicleInformation.as_view(), name='editvehicleinformation'),
    path('user/createengineoil/', CreateEngineOil.as_view(), name='createengineoil'),
    path('user/detailvehicle/<int:id>/',
         DetailVehicleInformation.as_view(), name='detailvehicle'),

    # urls for carwash
    #     path('user/createcarwash/',
    #          CreateCarWash.as_view(), name='createcarwash'),
    path('user/detailcarwash/<int:pk>/',
         DetailCarWash.as_view(), name='detailcarwash'),
    path('user/detelecarwash/<int:pk>/',
         DeleteCarWash.as_view(), name='detelecarwash'),
    path('user/editcarwash/<int:pk>/', EditCarWash.as_view(), name='editcarwash'),

    # urls for Subscriptions
    path('user/createsubscriptions/',
         CreateSubscription.as_view(), name='createsubscriptions'),
    path('user/detelesubscription/<int:pk>/',
         DeleteSubscription.as_view(), name='deletesubscription'),
    path('user/detailsubscription/<int:pk>/',
         DetailSubscription.as_view(), name='detailsubscription'),

    # urlls for Battery Order
    path('user/batteryorder/', BatteryOrderView.as_view(), name='batteryorder'),
    path('user/carwashorder/', CarWashOrderCreateView.as_view(), name='carwashorder'),
    path('user/carwasall/', CarWashOrderListView.as_view(), name='carwashall')

]
