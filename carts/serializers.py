from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from .models import Cart, CartProduct
from products.models import Product
from products.serializers import ProductSerializer

class CartProductSerializer(serializers.ModelSerializer):     
    class Meta:
        model = CartProduct
        fields = ('id', 'cart','product_quantity', 'product')
        read_only_fields = ['cart']

    def create(self, validated_data):
        cart, created = Cart.objects.get_or_create(user=validated_data['user'])
        cart_product = CartProduct.objects.filter(
            cart=cart,
            product=validated_data['product']
        ).first()
        if cart_product:
            raise ValidationError({"message": "O produto já existe no carrinho"})

        validated_data.pop('user', None)

        return CartProduct.objects.create(cart=cart, **validated_data)

    def update(self, instance, validated_data):
        instance.product_quantity = validated_data['product_quantity']
        instance.save()

        return instance
    
    
class CartProductListSerializer(serializers.ModelSerializer):  
    product = ProductSerializer()
    class Meta:
        model = CartProduct
        fields = ('id', 'cart','product_quantity', 'product')
        read_only_fields = ['cart']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user_id', 'cart_products')
        depth = 2
    
      