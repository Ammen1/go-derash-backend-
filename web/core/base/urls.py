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


    # urls for Subscriptions
    path('user/createsubscriptions/',
         CreateSubscription.as_view(), name='createsubscriptions'),
    path('user/detelesubscription/<int:pk>/',
         DeleteSubscription.as_view(), name='deletesubscription'),
    path('user/detailsubscription/<int:pk>/',
         DetailSubscription.as_view(), name='detailsubscription'),




]
