from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'account'

urlpatterns = [
    path('create/', Register.as_view(), name="create_user"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', GetUserView.as_view(), name='user'),
    path('users/', Allusers.as_view(), name='users'),
    path('deleteuser/<int:pk>/', DeteleUser.as_view(), name='deteleusers'),
    path('edituser/<int:pk>/', EditUser.as_view(), name='edituser'),


    path('drivers/', GetDrivers.as_view(), name='drivers'),
    path('driver/create/', CreateDriver.as_view(), name='drivers'),
    path('admin/', GetAdmins.as_view(), name='admin'),
    path('admin/create/', CreateAdmin.as_view(), name='create'),
]
