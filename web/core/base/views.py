from django.shortcuts import get_object_or_404
from core.base.models import *
from .serializers import *
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class CreateService(APIView):
    # parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceList(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceDaitle(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class EditService(generics.UpdateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class DeleteService(generics.RetrieveDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
