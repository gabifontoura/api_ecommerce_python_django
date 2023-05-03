from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Cart, CartProduct
from .serializers import CartSerializer, CartProductSerializer


class AddToCartView(generics.CreateAPIView):
    serializer_class = CartProductSerializer

    def perform_create(self, serializer):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        cart_product = CartProduct.objects.filter(
            cart=cart,
            product=serializer.validated_data['product']
        ).first()
        if cart_product:
            cart_product.product_quantity += serializer.validated_data['product_quantity']
            cart_product.save()
        else:
            serializer.save(cart=cart)


class RemoveFromCartView(generics.DestroyAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    def get_object(self):
        user = self.request.user
        cart = Cart.objects.filter(user=user).first()
        if not cart:
            raise generics.NotFound('Cart not found')
        product_id = self.kwargs['product_id']
        try:
            return CartProduct.objects.get(cart=cart, product_id=product_id)
        except CartProduct.DoesNotExist:
            raise generics.NotFound('Product not found in cart')

    def perform_destroy(self, instance):
        instance.delete()
