from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


from core.account.models import *
from .serializers import *


class Register(APIView):
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                refresh = RefreshToken.for_user(user)
                json = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserView(APIView):
    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(
            instance=user, context={'request': request})
        return Response(serializer.data)


class DeteleUser(generics.DestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = NewUser.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class Allusers(generics.ListAPIView):
    serializer_class = CustomAccountManager
    queryset = NewUser.objects.all()


class EditUser(generics.UpdateAPIView):
    serializer_class = CustomUserSerializer
    queryset = NewUser.objects.all()

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        if user is None:
            data = {
                'msg': "User is not found...!"
            }
            return Response(data)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
