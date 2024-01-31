from django.urls import path, include
from .views import *

app_name = 'carwash'

urlpatterns = [
    # urls for carwash
    path('user/carwash/create/', CarWashOrderCreateView.as_view(), name='create'),
    path('user/carwash/all/', CarWashOrderListView.as_view(), name='all'),
    path('user/carwash/detail/<int:pk>/',
         DetailCarWash.as_view(), name='detail'),
    path('user/carwash/detele/<int:pk>/',
         DeleteCarWash.as_view(), name='detele'),
    path('user/carwash/edit/<int:pk>/', EditCarWash.as_view(), name='edit'),

    # urls for category
    path('user/carwash/createcarcategory/',
         CreateCategory.as_view(), name='carcategory'),
    path('user/carwash/carallctegory/',
         ListCategory.as_view(), name='carallctegory'),
    path('user/carwash/detailcarcategory/<int:pk>/',
         DetailCategory.as_view(), name='detailcarcategory'),
    path('user/carwash/detelecarwashcategory/<int:pk>/',
         DeleteCategory.as_view(), name='detelecarwashcategory'),
    path('user/carwash/editcarwashcategory/<int:pk>/',
         UpdateCategory.as_view(), name='editcarwashcategory'),
]
