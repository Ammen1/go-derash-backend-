from core.checkout.models import DeliveryOptions
from core.tyre.basket import Basket
from rest_framework.decorators import api_view
from django.http import JsonResponse
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


@api_view(["POST"])
def basket_update_delivery(request):
    basket = Basket(request)

    try:
        delivery_option = str(request.data.get("deliveryoption"))
        delivery_type = DeliveryOptions.objects.get(id=delivery_option)
    except (ValueError, DeliveryOptions.DoesNotExist):
        return JsonResponse({"error": "Invalid delivery option"}, status=400)

    updated_total_price = basket.basket_update_delivery(
        delivery_type.delivery_price)

    session = request.session
    if "purchase" not in session:
        session["purchase"] = {
            "delivery_id": delivery_type.id,
        }
    else:
        session["purchase"]["delivery_id"] = delivery_type.id

    session.modified = True

    response_data = {
        "total": updated_total_price,
        "delivery_price": delivery_type.delivery_price
    }

    return JsonResponse(response_data)
