from django.urls import path, include
from .views import *

app_name = 'engineoil'

urlpatterns = [
    path('user/createengineoil/', CreateEngineOil.as_view(), name='createengineoil'),
    path('user/deleteengineoil/<int:id>/',
         DeleteEgineOil.as_view(), name='deleteengineoil'),
    path('user/allengineoil/', ListEngineOil.as_view(), name='allengineoil'),
    path('user/detailengineoil/<int:id>/',
         DetailEngineOil.as_view(), name='detailengineoil'),
    path('user/updateengineoil/<int:id>/',
         UpdateEngineOil.as_view(), name='updateengineoil'),
]
