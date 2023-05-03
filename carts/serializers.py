from rest_framework import serializers
from .models import Cart, CartProduct



class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('id', 'product_quantity', 'product')



class CartSerializer(serializers.ModelSerializer):
    cart_products = CartProductSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ('id', 'user_id', 'products', 'cart_products')


