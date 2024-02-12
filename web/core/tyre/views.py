from paypalcheckoutsdk.orders import OrdersGetRequest
from .paypal import PayPalClient
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from core.tyre.basket import Basket
from core.checkout.models import DeliveryOptions
from .models import *
from .serializers import *
import json


class TyreAllAPIView(generics.ListAPIView):
    queryset = Tyre.objects.filter(
        is_active=True)
    serializer_class = TyreSerializer


class TyreCategoryListAPIView(APIView):
    def get(self, request, category_slug=None, format=None):
        category = get_object_or_404(TyreCategory, slug=category_slug)
        tyres = Tyre.objects.filter(
            category__in=category.get_descendants(include_self=True)
        )
        serializer = TyreSerializer(tyres, many=True)
        return Response({'category': category.name, 'tyres': serializer.data}, status=status.HTTP_200_OK)


class TyreDetailAPIView(generics.RetrieveAPIView):
    queryset = Tyre.objects.filter(is_active=True)
    serializer_class = TyreSerializer
    lookup_field = 'slug'


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


class AddToOrderView(APIView):
    # {
    #     "action": "post",
    #     "full_name": "Ganaral Hospital",
    #     "email": "aaaa@aaaa.com",
    #     "address": "jimma",
    #     "city": "addis abaab",
    #     "phone": "09443654",
    #     "total_paid": 10.03,
    #     "order_key": "order_key1",
    #     "payment_option": "option2",
    #     "billing_status": true
    # }
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        basket = Basket(request)

        print("request.data", request.data)  # Add this line for debugging

        if request.data.get("action") == "post":
            order_key = request.data.get("order_key")
            user_id = request.user.id
            basket_total = basket.get_total_price()
            print("basket_total", basket_total)

            try:
                # Check if order exists
                order = Order.objects.get(order_key=order_key)
            except Order.DoesNotExist:
                # Order doesn't exist, create a new one
                order = Order.objects.create(
                    user_id=user_id,
                    full_name="name",
                    address="add",
                    total_paid=basket_total,
                    order_key=order_key,
                )

                # Create order items
                for item in basket:
                    product = item["item"]
                    # Retrieve Tyre object based on your product information
                    tyre = Tyre.objects.get(id=product['id'])
                    print("tyre", tyre)
                    OrderItem.objects.create(
                        order=order, product=tyre, unit_price=item["price"], quantity=item["qty"]
                    )

                # Clear the basket after the order is created
                basket.clear()

                # Return a success response
                response_data = {"success": "Order placed successfully"}
                return Response(response_data, status=status.HTTP_201_CREATED)

            # Order already exists, return an error response
            return Response({"error": "Order with this key already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Invalid action, return a generic error response
        return Response({"error": "Invalid request. 'action' parameter missing or not equal to 'post'."}, status=status.HTTP_400_BAD_REQUEST)


class PaymentConfirmationView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        order_key = request.data.get("order_key")
        order = get_object_or_404(Order, order_key=order_key)
        order.billing_status = True
        order.save()
        return Response({"success": "Payment confirmation received"})


class UserOrdersView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        print(f"User ID: {user_id}")
        queryset = Order.objects.filter(user_id=user_id, billing_status=True)
        print(f"Queryset: {queryset}")
        return queryset


class BasketAddView(APIView):
    def post(self, request, *args, **kwargs):
        basket = Basket(request)
        if request.data.get("action") == "post":
            product_id = int(request.data.get("productid"))
            product_qty = int(request.data.get("productqty"))
            product = get_object_or_404(Tyre, id=product_id)
            product_price = product.regular_price

            basket.add(item=product, qty=product_qty, price=product_price)

            basket_qty = len(basket)
            response_data = {"qty": basket_qty}
            return Response(response_data, status=status.HTTP_200_OK)

        return Response({"error": "Invalid request. 'action' parameter missing or not equal to 'post'."}, status=status.HTTP_400_BAD_REQUEST)


class BasketDeleteView(APIView):
    def post(self, request, *args, **kwargs):
        basket = Basket(request)
        if request.data.get("action") == "post":
            product_id = int(request.data.get("productid"))

            basket.delete(item=product_id)

            basket_qty = len(basket)
            basket_total = basket.get_total_price()
            response_data = {"qty": basket_qty, "subtotal": basket_total}
            return Response(response_data, status=status.HTTP_200_OK)

        return Response({"error": "Invalid request. 'action' parameter missing or not equal to 'post'."}, status=status.HTTP_400_BAD_REQUEST)


class BasketUpdate(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        basket = Basket(request)

        if request.data.get("action") == "post":
            product_id = int(request.data.get("productid"))
            product_qty = int(request.data.get("productqty"))
            basket.update(product=product_id, qty=product_qty)

            basket_qty = len(basket)
            print("Basket Quantity:", basket_qty)
            basket_subtotal = basket.get_subtotal_price()
            print("Basket Subtotal:", basket_subtotal)
            response = {"qty": basket_qty, "subtotal": basket_subtotal}
            return Response(response, status=status.HTTP_200_OK)

        return Response({"error": "Invalid request. 'action' parameter missing or not equal to 'post'."}, status=status.HTTP_400_BAD_REQUEST)


class PaymentCompleteView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        order_id = data.get("orderID")
        user_id = request.user.id

        # Initialize PayPal client
        PPClient = PayPalClient()

        # Execute PayPal request
        requestorder = OrdersGetRequest(order_id)
        response = PPClient.client.execute(requestorder)

        # Ensure response is successful before accessing its attributes
        if response.result.purchase_units:
            print(response.result.purchase_units)
            total_paid = response.result.purchase_units[0].amount.value
        else:
            return Response("Invalid PayPal response", status=status.HTTP_400_BAD_REQUEST)

        # Initialize Basket
        basket = Basket(request)

        order_data = {
            "user_id": user_id,
            "full_name": response.result.purchase_units[0].shipping.name.full_name,
            "email": response.result.payer.email_address,
            "address": response.result.purchase_units[0].shipping.address.address,
            "total_paid": total_paid,
            "order_key": response.result.id,
            "payment_option": "paypal",
            "billing_status": True,
        }

        # Serialize order data
        order_serializer = OrderSerializer(data=order_data)
        order_serializer.is_valid(raise_exception=True)
        order = order_serializer.save()

        order_id = order.pk

        for item in basket:
            order_item_data = {
                "order_id": order_id,
                "product": item["product"],
                "price": item["price"],
                "quantity": item["qty"],
            }

            # Serialize order item data
            order_item_serializer = OrderItemSerializer(data=order_item_data)
            order_item_serializer.is_valid(raise_exception=True)
            order_item_serializer.save()

        return Response("Payment completed!", status=status.HTTP_200_OK)
