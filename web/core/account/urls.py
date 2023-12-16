from django.urls import path, include
from .views import *

app_name = 'account'

urlpatterns = [
    path('create/', Register.as_view(), name="create_user"),
    # path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
    # path('userdetail/', UserDetail.as_view(), name='userdetail'),
    path('user/', GetUserView.as_view(), name='user'),
    path('users/', Allusers.as_view(), name='users'),
    path('deleteuser/<int:pk>/', DeteleUser.as_view(), name='deteleusers'),
    path('edituser/<int:pk>/', EditUser.as_view(), name='edituser'),
]
