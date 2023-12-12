from django.urls import path
from . views import *


app_name = 'base'

urlpatterns = [
    # Admin urls
    path('admin/createservices/', CreateService.as_view(), name='createservice'),
    path('admin/listcreate/', ServiceList.as_view(), name='listservice'),
    path('admin/detailservice/<int:id>/',
         ServiceDaitle.as_view(), name='detailservice'),
    path('admin/editservices/<int:pk>/',
         EditService.as_view(), name='editservices'),
    path('admin/deleteservice/<int:pk>/',
         DeleteService.as_view(), name='deleteservice'),
    path('admin/listvehicleinformation', ListVehicleInformation.as_view(),
         name='listvehicleinformation'),
    path('admin/deletevehicleinformation/<int:id>/',
         DeleteVehucleInformation, name='deletevehicleinformation'),
    path('admin/createservicetype',
         CreateServiceType.as_view(), name='createservicetype'),
    path('admin/listservicetype', ListServiceType.as_view(), name='listservicetype'),
    path('admin/detilservicetype/<int:id>/',
         DetailServiceType.as_view(), name='detailseervide'),
    path('admin/deleteservicety<int:id>/',
         DeleteServiceType.as_view(), name='deleteservicety'),


    # Users urls
    path('user/createvehicleinfrmation/',
         CreateVehicleInformation.as_view(), name='createvehicleInformation'),
    path('user/editvehicleinformation/<int:int>/',
         EditVehicleInformation.as_view(), name='editvehicleinformation'),
    path('')


]
