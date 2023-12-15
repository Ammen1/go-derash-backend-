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
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetUserView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serialized_user = CustomUserSerializer(context={'request': request})
        return Response(serialized_user.data)


class UserDetail(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomUserSerializer
    queryset = NewUser.objects.all()

    def get(self, request, *args, **kwargs):
        user_count = self.get_queryset().count()
        data = {
            'user_count': user_count,
        }
        return Response(data)


class Allusers(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = NewUser.objects.all()

    # def get(self, request, *args, **kwargs):
    #     users = self.get_queryset()
    #     data = {
    #         'users': users,
    #     }
    #     return Response(data)


class DeteleUser(generics.DestroyAPIView):
    serializer_class = CustomUserSerializer
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