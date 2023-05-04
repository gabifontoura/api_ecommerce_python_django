from rest_framework import serializers

from carts.models import Cart, CartProduct
from .models import Order

from products.serializers import ProductSerializer
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "seller_id", "product", "user"]
        read_only_fields = ["id", "created_at", "seller_id"]

    # def create(self, validated_data):
    #     cart = get_object_or_404(Cart, user=validated_data['user'])

    #     cart_product = CartProduct.objects.filter(
    #         cart=cart
    #     )

    #     if not cart_product:
    #         raise ValidationError({"message": "O carrinho está vazio"})
        
    #     products_list = set(cart_product)

    #     products_list.forEach()
        

        
    #     return 