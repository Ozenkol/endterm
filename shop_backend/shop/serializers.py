from rest_framework import serializers
from .models import User, Product, Cart, CartItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'avatar']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "discount_percentage",
            "rating",
            "stock",
            "brand",
            "category",
            "thumbnail",
            "images",
        ]

class ProductResponseSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    skip = serializers.SerializerMethodField()
    limit = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('products', 'total', 'skip', 'limit')
    def get_products(self, obj):
        products = Product.objects.all()
        return products
    def get_total(self, obj):
        total = len(Product.objects.all())
        return total
    def get_skip(self, obj):
        return 30
    def get_limit(self, obj):
        return 0


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ["product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "items"]