from django.urls import path
from . views import *


app_name = 'base'

urlpatterns = [
    path('admin/create/', CreateService.as_view(), name='createservice'),
    path('admin/listcreate/', ServiceList.as_view(), name='listservice'),
    
]
