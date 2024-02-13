from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from core.basket.basket import Basket
from core.orders.models import Order, OrderItem
from core.orders.serializers import OrderItemSerializer, OrderSerializer


# {
#     "action": "post",
#     "full_name": "John Doe",
#     "email": "john.doe@example.com",
#     "address": "123 Main St",
#     "city": "Cityville",
#     "phone": "555-1234",
#     "total_paid": 100.50,
#     "order_key": "order_key_123",
#     "payment_option": "option2",
#     "billing_status": true

# }
# http://127.0.0.1:8000/api/tyre/order/add/


class AddToOrder(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        basket = Basket(request)

        print("request.data", request.data)

        # Check if the action is 'post'
        if request.data.get("action") == "post":
            order_key = request.data.get("order_key")
            user_id = request.user.id
            basket_total = basket.get_total_price()

            try:
                # Check if order exists
                order = Order.objects.get(order_key=order_key)
            except Order.DoesNotExist:
                # Order doesn't exist, create a new one
                order = Order.objects.create(
                    user_id=user_id,
                    full_name=request.data.get("full_name", ""),
                    email=request.data.get("email", ""),
                    address=request.data.get("address", ""),
                    city=request.data.get("city", ""),
                    phone=request.data.get("phone", ""),
                    total_paid=basket_total,
                    order_key=order_key,
                    payment_option=request.data.get("payment_option", ""),
                    billing_status=request.data.get("billing_status", False)
                )

            for item in basket:
                OrderItem.objects.create(
                    order=order, product=item["product"], unit_price=item["price"], quantity=item["qty"]
                )

                basket.clear()

                response_data = {"success": "Order placed successfully"}
                return Response(response_data, status=status.HTTP_201_CREATED)

            return Response({"error": "Order with this key already exists"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"error": "Invalid request. 'action' parameter missing or not equal to 'post'."}, status=status.HTTP_400_BAD_REQUEST)


class PaymentConfirmation(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        order_key = request.data.get("order_key")
        order = get_object_or_404(Order, order_key=order_key)
        order.billing_status = True
        order.save()
        return Response({"success": "Payment confirmation received"})


class UserOrders(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        print(f"User ID: {user_id}")
        queryset = Order.objects.filter(user_id=user_id, billing_status=True)
        print(f"Queryset: {queryset}")
        return queryset
