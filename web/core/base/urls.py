# your_app/urls.py

from django.urls import path, include
from .views import *

app_name = 'base'  # Replace 'your_app' with your actual app name

urlpatterns = [
    # Admin URLs
    path('admin/createservices/', CreateCategory.as_view(), name='createservice'),
    path('admin/listservices/', ServiceList.as_view(), name='listservice'),
    path('admin/detailservice/<int:pk>/',
         ServiceDetail.as_view(), name='detailservice'),
    path('admin/editservices/<int:pk>/',
         EditService.as_view(), name='editservices'),
    path('admin/deleteservice/<int:pk>/',
         DeleteService.as_view(), name='deleteservice'),

    # Vehicle Information URLs
    path('admin/listvehicleinformation/',
         ListVehicleInformation.as_view(), name='listvehicleinformation'),
    path('admin/deletevehicleinformation/<int:pk>/',
         DeleteVehicleInformation.as_view(), name='deletevehicleinformation'),

    # Service Type URLs
    path('admin/createservicetype/',
         CreateServiceType.as_view(), name='createservicetype'),
    path('admin/listservicetype/',
         ListServiceType.as_view(), name='listservicetype'),
    path('admin/detilservicetype/<int:pk>/',
         DetailServiceType.as_view(), name='detailseervide'),
    path('admin/deleteservicetype/<int:pk>/',
         DeleteServiceType.as_view(), name='deleteservicetype'),

    # Tyre URLs
    path('admin/tyre/create/', CreateTyre.as_view(), name='create_tyre'),
    path('admin/tyre/list/', ListTyre.as_view(), name='list_tyre'),
    path('admin/tyre/detail/<int:pk>/', DetailTyre.as_view(), name='detail_tyre'),
    path('admin/tyre/delete/<int:pk>/', DeleteTyre.as_view(), name='delete_tyre'),
    path('admin/tyre/edit/<int:pk>/', EditTyre.as_view(), name='edit_tyre'),

    # CarWah URLS
    path('admin/listcarwash/', ListCarWash.as_view(), name='listcarwash'),

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

    #     path('user/createbooking/', CreateBooking.as_view(), name='createbooking'),
    #     path('user/editbooking/<int:pk>/', EditBooking.as_view(), name='editbooking'),
    #     path('user/deletebooking/<int:pk>/',
    #          EditBooking.as_view(), name='deletebooking'),
    #     path('user/detailbooking/<int:pk>/',
    #          EditBooking.as_view(), name='detailbooking'),

    # urls for carwash
    path('user/createcarwash/',
         CreateCarWash.as_view(), name='createcarwash'),
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
         DetailSubscription.as_view(), name='detailsubscription')

]
