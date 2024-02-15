# your_app/urls.py

from django.urls import path, include
from .views import *

app_name = 'base'

urlpatterns = [
    path('products/all/',
         Product_all.as_view(), name='product_all'),
    path('products/category/<str:category_slug>/',
         Category_list.as_view(), name='tyre-category-list'),
    path('product/detail/<str:slug>/',
         Product_detail.as_view(), name='tyre-detail'),
]
