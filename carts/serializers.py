from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Cart, CartProduct



class CartProductSerializer(serializers.ModelSerializer):  
    class Meta:
        model = CartProduct
        fields = ('id', 'cart_id','product_quantity', 'product_id')
        read_only = ['cart_id']

    def get(self, validated_data):
        cart = get_object_or_404(Cart, user=validated_data['user'])
        # get_object_or_404(Cart.objects.filter(user=self.request.user))

        cart_products = CartProduct.objects.filter(
            cart=cart
        )

        import ipdb
        ipdb.set_trace()

        return cart_products

    def create(self, validated_data):
        cart, created = Cart.objects.get_or_create(user=validated_data['user'])
        cart_product = CartProduct.objects.filter(
            cart=cart,
            product=validated_data['product']
        ).first()
        if cart_product:
            raise ValueError("O produto já existe no carrinho")

        validated_data.pop('user', None)

        return CartProduct.objects.create(cart=cart, **validated_data)
 
    def update(self, instance, validated_data):
        instance.product_quantity = validated_data['product_quantity']
        instance.save()
        return instance


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ('id', 'user_id', 'cart_products')
        depth = 2
    
      