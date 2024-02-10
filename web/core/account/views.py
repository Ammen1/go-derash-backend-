from rest_framework import generics
from .serializers import CustomUserSerializer
from rest_framework import status
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from core.account.models import *
from .serializers import *


class CreateAdmin(generics.CreateAPIView):
    serializer_class = AdminUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateDriver(generics.CreateAPIView):
    serializer_class = DriverSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Register(generics.CreateAPIView):
    serializer_class = CustomUserSerializer

    def generate_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return tokens

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                tokens = self.generate_tokens(user)
                return Response(tokens, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarCreateView(APIView):
    def get_user(self, user_id):
        try:
            return NewUser.objects.get(id=user_id)
        except NewUser.DoesNotExist:
            return None

    def post(self, request, user_id):
        user = self.get_user(user_id)
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllCars(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class GetUserView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = NewUser.objects.all()


class GetDrivers(generics.ListAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class GetAdmins(generics.ListAPIView):
    serializer_class = AdminUserSerializer
    queryset = AdminUser.objects.all()


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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['phone'] = user.phone
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
