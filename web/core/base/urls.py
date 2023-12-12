from django.urls import path
from . views import *


app_name = 'base'

urlpatterns = [
    # Admin urls
    path('admin/createservices/', CreateService.as_view(), name='createservice'),
    # http://127.0.0.1:8000/api/base/admin/createservices/
    path('admin/listservices/', ServiceList.as_view(), name='listservice'),
    # http://127.0.0.1:8000/api/base/admin/listservices/
    path('admin/detailservice/<int:pk>/',
         ServiceDaitle.as_view(), name='detailservice'),
    # http://127.0.0.1:8000/api/base/admin/detailservice/id
    path('admin/editservices/<int:pk>/',
         EditService.as_view(), name='editservices'),
    # http://127.0.0.1:8000/api/base/admin/editservices/id/
    path('admin/deleteservice/<int:pk>/',
         DeleteService.as_view(), name='deleteservice'),
    # http://127.0.0.1:8000/api/base/admin/deleteservice/id/
    path('admin/listvehicleinformation', ListVehicleInformation.as_view(),
         name='listvehicleinformation'),
    # http://127.0.0.1:8000/api/base/admin/listvehicleinformation/
    path('admin/deletevehicleinformation/<int:pk>/',
         DeleteVehucleInformation.as_view(), name='deletevehicleinformation'),
    # http://127.0.0.1:8000/api/base/admin/deletevehicleinformation/id/
    path('admin/createservicetype',
         CreateServiceType.as_view(), name='createservicetype'),
    # http://127.0.0.1:8000/api/base/admin/createservicetype/
    path('admin/listservicetype', ListServiceType.as_view(), name='listservicetype'),
    # http://127.0.0.1:8000/api/base/admin/listservicetype/
    path('admin/detilservicetype/<int:pk>/',
         DetailServiceType.as_view(), name='detailseervide'),
    # http://127.0.0.1:8000/api/base/admin/detilservicetype/id/
    path('admin/deleteservicetype/<int:pk>/',
         DeleteServiceType.as_view(), name='deleteservicetype'),
    # http://127.0.0.1:8000/api/base/admin/deleteservicetype/id/

    # Users urls
    path('user/createvehicleinfrmation/',
         CreateVehicleInformation.as_view(), name='createvehicleInformation'),
    # http://127.0.0.1:8000/api/base/user/createvehicleinfrmation/
    path('user/editvehicleinformation/<int:pk>/',
         EditVehicleInformation.as_view(), name='editvehicleinformation'),
    # http://127.0.0.1:8000/api/base/admin/editvehicleinformation/id/
    path('user/createengineoil', CreateEngineOil.as_view(), name='createengineoil'),
    # http://127.0.0.1:8000/api/base/admin/createengineoil/id/
    path('user/createbooking/',
         CreateBooking.as_view(), name='createbooking'),
    # http://127.0.0.1:8000/api/base/user/createbooking/
    path('user/editbooking/<int:pk>/',
         EditBooking.as_view(), name='editbooking'),
    # http://127.0.0.1:8000/api/base/user/editbooking/id/
    path('user/detelebooking/<int:pk>/',
         EditBooking.as_view(), name='deletebooking'),
    # http://127.0.0.1:8000/api/base/admin/detelebooking/id/
    path('user/detailbooking/<int:pk>/',
         EditBooking.as_view(), name='detailbooking'),
    # http://127.0.0.1:8000/api/base/admin/detelebooking/id/


]
