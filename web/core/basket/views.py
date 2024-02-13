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
from core.basket.basket import Basket
from core.base.models import Product

from .serializers import *
import json


class Basket_Summary(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        basket = Basket(request)
        return Response(basket, status=status.HTTP_200_OK)
# {
# "action": "post"
# "productid": 1,
# "productqty": 3
# }


class BasketAdd(APIView):
    def post(self, request, *args, **kwargs):
        basket = Basket(request)
        if request.data.get("action") == "post":
            product_id = int(request.data.get("productid"))
            product_qty = int(request.data.get("productqty"))
            product = get_object_or_404(Product, id=product_id)
            product_price = product.regular_price

            basket.add(product=product, qty=product_qty)

            basket_qty = len(basket)
            response_data = {"qty": basket_qty}
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


class BasketDelete(APIView):
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
