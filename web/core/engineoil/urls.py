from django.urls import path, include
from .views import *

app_name = 'engineoil'

urlpatterns = [
    # urls for engineoil
    path('user/createengineoil/', CreateEngineOil.as_view(), name='createengineoil'),
    path('user/deleteengineoil/<int:pk>/',
         DeleteEgineOil.as_view(), name='deleteengineoil'),
    path('user/allengineoil/', ListEngineOil.as_view(), name='allengineoil'),
    path('user/detailengineoil/<int:id>/',
         DetailEngineOil.as_view(), name='detailengineoil'),
    path('user/updateengineoil/<int:id>/',
         UpdateEngineOil.as_view(), name='updateengineoil'),
    # urls for engineoilcategory
    path('user/createengineoilcategory/',
         CreateEngineOilCategory.as_view(), name='createengineoilcategory'),
    path('user/deleteengineoilcategory/<int:id>/',
         DeleteEngineOilCategory.as_view(), name='deleteengineoilcategory'),
    path('user/allengineoilcategory/',
         ListEngineOilCategory.as_view(), name='allengineoilcategory'),
    path('user/detailengineoilcategory/<int:id>/',
         DetailEngineOilCategory.as_view(), name='detailengineoilcategory'),
    path('user/updateengineoilcategory/<int:id>/',
         UpdateEngineOilCategory.as_view(), name='updateengineoilcategory'),
    # urls for engineoilbrand
    path('user/createengineoilbrand/',
         CreateEngineOilBrand.as_view(), name='createengineoilbrand'),
    path('user/deleteengineoilbrand/<int:id>/',
         DeleteEngineOilBrand.as_view(), name='deleteengineoilbrand'),
    path('user/allengineoilbrand/',
         ListEngineOilBrand.as_view(), name='allengineoilcategory'),
    path('user/detailengineoilbrand/<int:id>/',
         DetailEngineOilBrand.as_view(), name='detailengineoilbrand'),
    path('user/updateengineoilbrand/<int:id>/',
         UpdateEngineOilBrand.as_view(), name='updateengineoilbrand'),
]
