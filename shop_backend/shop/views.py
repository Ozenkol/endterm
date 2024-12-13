from django.shortcuts import render
from django.core import serializers
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView, Response
from .models import User, Product, Cart, CartItem
from .serializers import UserSerializer, ProductSerializer, CartSerializer, ProductResponseSerializer
from django.http import JsonResponse

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class ProductResponse(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        products = ProductSerializer(Product.objects.all(), many=True)
        response_data = {
            'products': products.data,
            'total': len(Product.objects.all()),
            'skip': 10,
            'limit': 0
        }
        return Response(response_data)
    
class ProductSingle(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, id):
        product = Product.objects.get(pk = id)
        response_data = ProductSerializer(product)
        return Response(response_data.data)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.prefetch_related("items__product").all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]