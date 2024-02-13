from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from core.basket.basket import Basket
from core.orders.models import Order
from core.orders.serializers import OrderSerializer
from core.checkout.models import DeliveryOptions, PaymentSelections
from core.checkout.serializers import DeliveryOptionsSerializer, PaymentSelectionsSerializer


class PaymentConfirmation(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        order_key = request.data.get("order_key")
        order = get_object_or_404(Order, order_key=order_key)
        order.billing_status = True
        order.save()
        return Response({"success": "Payment confirmation received"})


# {
#     "action": "post",
#     "deliveryoption": 1
# }


class Basket_Update_Delivery(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        basket = Basket(request)

        if request.data.get("action") == "post":
            delivery_option_id = request.data.get("deliveryoption")

            try:
                delivery_type = DeliveryOptions.objects.get(
                    id=delivery_option_id)
            except DeliveryOptions.DoesNotExist:
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
            return Response(response_data, status=status.HTTP_201_CREATED)

        # If the action is not "post", return an error response
        return Response({"error": "Invalid request. 'action' parameter missing or not equal to 'post'."}, status=status.HTTP_400_BAD_REQUEST)


class DummyPaymentGatewayClient:
    def get_order_details(self, order_id):
        # Simulate a successful payment response
        return {
            "successful": True,
            "total_amount": 100.0,
            "shipping_address": {
                "full_name": "Amen Abush",
                "email": "Abudh@amen.com",
                "address": "Addis Adu genet ",
            },
        }


class PaymentComplete(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        basket = Basket(request)

        # Simulate a successful payment response
        payment_gateway_client = DummyPaymentGatewayClient()
        payment_response = payment_gateway_client.get_order_details(
            "dummy_order_id")

        if payment_response["successful"]:
            # Extract relevant information from the payment response
            total_paid = payment_response["total_amount"]
            shipping_address = payment_response["shipping_address"]

            # Prepare order data
            order_data = {
                # "user_id": user.id,
                "full_name": shipping_address["full_name"],
                "email": shipping_address["email"],
                "address": shipping_address["address"],
                "total_paid": total_paid,
                "order_key": "order_key_123",
                "payment_option": "option2",
                "billing_status": True,
                "orderID": 52,
                "user": 1,
                "city": "Cityville",
                "phone": "555-123 4",
            }

            # Serialize order data
            order_serializer = OrderSerializer(data=order_data)
            order_serializer.is_valid(raise_exception=True)
            order = order_serializer.save()

            order_id = order.pk

            # Iterate through basket items and save order items
            for item in basket:
                order_item_data = {
                    "order_id": order_id,
                    "product": item["product"],
                    "price": item["price"],
                    "quantity": item["qty"],
                }

                # Serialize order item data
                order_item_serializer = OrderItemSerializer(
                    data=order_item_data)
                order_item_serializer.is_valid(raise_exception=True)
                order_item_serializer.save()

            # Clear the basket after the order is created
            basket.clear()

            return Response("Payment completed!", status=status.HTTP_200_OK)
        else:
            return Response("Invalid payment response", status=status.HTTP_400_BAD_REQUEST)
