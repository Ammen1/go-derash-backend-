from django.urls import path, include
from .views import *

app_name = 'carwash'

urlpatterns = [
    # urls for carwash
    path('user/carwashorder/', CarWashOrderCreateView.as_view(), name='carwashorder'),
    path('user/carwasall/', CarWashOrderListView.as_view(), name='carwashall'),
    path('user/detailcarwash/<int:pk>/',
         DetailCarWash.as_view(), name='detailcarwash'),
    path('user/detelecarwash/<int:pk>/',
         DeleteCarWash.as_view(), name='detelecarwash'),
    path('user/editcarwash/<int:pk>/', EditCarWash.as_view(), name='editcarwash'),

    # urls for category
    path('user/carcategory/', CreateCategory.as_view(), name='carcategory'),
    path('user/carallctegory/', ListCategory.as_view(), name='carallctegory'),
    path('user/detailcarcategory/<int:pk>/',
         DetailCategory.as_view(), name='detailcarcategory'),
    path('user/detelecarwashcategory/<int:pk>/',
         DeleteCategory.as_view(), name='detelecarwashcategory'),
    path('user/editcarwashcategory/<int:pk>/',
         UpdateCategory.as_view(), name='editcarwashcategory'),
]
