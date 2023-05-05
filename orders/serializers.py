from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from carts.models import Cart, CartProduct
from orders.models import Order
from products.models import Product
from users.models import User

from django.core.mail import send_mail
from django.conf import settings

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "seller_id", "product", "user"]
        read_only_fields = ["id", "created_at", "seller_id", "user"]

    def create(self, validated_data):
        cart = get_object_or_404(Cart, user=validated_data['user'])

        cart_product = CartProduct.objects.filter(
            cart=cart,
            product=validated_data['product']
        ).first()

        cart_product = get_object_or_404(CartProduct, cart=cart,
            product=validated_data['product'] )

        if cart_product.product_quantity > cart_product.product.quantity:
                data = {
                    "name": cart_product.product.name,
                    "product_quantity": cart_product.product_quantity,
                    "available_quantity": cart_product.product.quantity
                }

                raise ValidationError({"message": "Quantidade do produto indisponível",
                                   "result": [data]
                                   })
        
        order = Order.objects.create(
            user= validated_data['user'],
            seller_id= cart_product.product.seller_id,
            product= {
                "id": f"{cart_product.product.id}",
                "name": cart_product.product.name,
                "category":cart_product.product.category,
                "value":f"{cart_product.product.value}",
                "image":cart_product.product.image,
                "quantity":f"{cart_product.product_quantity}"
            },
            status="Pedido Realizado"
        )

        product_instance = Product.objects.filter(pk = cart_product.product.id).first()

        product_instance.quantity -= cart_product.product_quantity

        if product_instance.quantity == 0:
            product_instance.is_available = False

        product_instance.save()

        cart_product.delete()

        return order
    

    def update(self, instance: Order, validated_data: dict):
        instance.status = validated_data['status']
        instance.save()

        send_mail(
            subject = 'Atualização do seu pedido',
            message = f'O status do pedido {instance.product["name"]} foi atualizado para {instance.status}',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [instance.user.email],
            fail_silently = False
        )
        
        return instance