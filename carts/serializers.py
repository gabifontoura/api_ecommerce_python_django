from rest_framework import serializers
from .models import Cart, CartProduct



class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('id', 'product_quantity', 'product')

    # def get(self, validated_data):
    #     cart = Cart.objects.get(user=validated_data['user'])

    #     cart_products = CartProduct.objects.filter(
    #         cart=cart,
    #     )


    def create(self, validated_data):
        cart, created = Cart.objects.get_or_create(user=validated_data['user'])
        cart_product = CartProduct.objects.filter(
            cart=cart,
            product=validated_data['product']
        ).first()
        if cart_product:
            raise ValueError("O produto já existe no carrinho")

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
    
      