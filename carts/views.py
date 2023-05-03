from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Cart, CartProduct
from .serializers import CartSerializer, CartProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class AddToCartView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartProductSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
 


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    # def get_object(self):
    #     user = self.request.user
    #     cart_product = CartProduct.objects.filter(user=user).first()
    #     if not cart_product:
    #         raise generics.NotFound('Cart not found')
    #     product_id = self.kwargs['product_id']
    #     try:
    #         return CartProduct.objects.get(cart=cart_product, product_id=product_id)
    #     except CartProduct.DoesNotExist:
    #         raise generics.NotFound('Product not found in cart')

    # def perform_destroy(self, instance):
    #     instance.delete()
