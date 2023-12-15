from rest_framework import generics
from .models import DeliveryOptions, PaymentSelections
from .serializers import DeliveryOptionsSerializer, PaymentSelectionsSerializer


class DeliveryOptionsListCreateView(generics.ListCreateAPIView):
    queryset = DeliveryOptions.objects.all()
    serializer_class = DeliveryOptionsSerializer


class DeliveryOptionsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryOptions.objects.all()
    serializer_class = DeliveryOptionsSerializer


class PaymentSelectionsListCreateView(generics.ListCreateAPIView):
    queryset = PaymentSelections.objects.all()
    serializer_class = PaymentSelectionsSerializer


class PaymentSelectionsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentSelections.objects.all()
    serializer_class = PaymentSelectionsSerializer
