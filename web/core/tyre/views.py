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
from .models import *
from .serializers import *


class TyreAllAPIView(generics.ListAPIView):
    queryset = Tyre.objects.filter(
        is_active=True).prefetch_related("tyre_image")
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


class AddToOrderView(APIView):
    def post(self, request, *args, **kwargs):
        basket = Basket(request)

        print(request.data)  # Add this line for debugging

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
                    full_name="name",  # Replace with actual full name logic
                    address="add",  # Replace with actual address logic
                    total_paid=basket_total,
                    order_key=order_key,
                )

                # Create order items
                for item in basket:
                    product = item["item"]
                    OrderItem.objects.create(
                        order=order, product=product, price=item["price"], quantity=item["qty"]
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
