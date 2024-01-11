from django.urls import path, include
from .views import *

app_name = 'fuel'

urlpatterns = [
    # Fuel URLS
    path('user/fuel/create/', FuelOrderCreateView.as_view(), name='create'),
    path('user/fuel/all/', ListFuel.as_view(), name='allfuel'),
    path('user/fuel/detail/<int:pk>/',
         DetailGasline.as_view(), name='detailfuel'),
    path('user/fuel/detele/', DeleteGasline.as_view(), name='detelefuel'),
    path('user/fuel/edit/', UpdateGasline.as_view(), name='editfuel'),
    # FuelCategory URLS
    path('user/fuel/createfuelcategory/',
         CreateFuelCategory.as_view(), name='createfuelcategory'),
    path('user/fuel/allfuelcategory/',
         ListFuelCategory.as_view(), name='allfuelcategory'),
    path('user/fuel/detailfuelcategory/<int:pk>/',
         DetailFuelCategory.as_view(), name='detailfuelcategory'),
    path('user/fuel/detelefuelcategory/',
         DeleteFuelCategory.as_view(), name='detelefuelcategory'),
    path('user/fuel/editfuelcategory/',
         UpdateFuelCategory.as_view(), name='editfuelcategory'),
    # FuelBrand URLS
    path('user/fuel/createfuelbrand/',
         CreateFuelBrand.as_view(), name='createfuelbrand'),
    path('user/fuel/allfuelbrand/',
         ListFuelBrand.as_view(), name='allfuelbrand'),
    path('user/fuel/detailfuelbrand/<int:pk>/',
         DetailFuelBrand.as_view(), name='detailfuelbrand'),
    path('user/fuel/detelefuelbrand/',
         DeleteFuelBrand.as_view(), name='detelefuelbrand'),
    path('user/fuel/editfuelbrand/',
         UpdateFuelBrand.as_view(), name='editfuelbrand'),

]
