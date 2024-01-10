from django.urls import path, include
from .views import *

app_name = 'battery'

urlpatterns = [
    path('user/batteryorder/', BatteryOrderView.as_view(), name='batteryorder'),
    path('user/allbattery/', ListBattery.as_view(), name="allbattery"),
    path('user/detailbattery/<int:pk>/',
         DetailBattery.as_view(), name="detailbattery"),
    path('user/detelebattery/<int:pk>/',
         DeleteBattery.as_view(), name="detelebattery"),
    paht('user/updatebattery/<int:pk>/',
         UpdateBattery.as_view(), name="updatebattery"),
    # ursl for Brand
    path('user/batterybrand/', BatteryBrand.as_view(), name='batterybrand'),
    path('user/allbrand/', ListBrand.as_view(), name="allbrand"),
    path('user/detailbrand/<int:pk>/',
         DetailBrand.as_view(), name="detailbrand"),
    path('user/detelebrand/<int:pk>/',
         DeleteBrand.as_view(), name="detelebrand"),
    paht('user/updatebrand/<int:pk>/',
         UpdateBrand.as_view(), name="updatebrand"),

    # urls for Category
    path('user/batterycategory/', BatteryCategory.as_view(), name='batterycategory'),
    path('user/allcategory/', ListBatteryCategory.as_view(), name="allcategory"),
    path('user/detailcategory/<int:pk>/',
         DetailBatteryCategory.as_view(), name="detailcategory"),
    path('user/detelecategory/<int:pk>/',
         DeleteBatteryCategory.as_view(), name="detelecategory"),
    paht('user/updatecategory/<int:pk>/',
         UpdateBatteryCategory.as_view(), name="updatecategory"),

]
