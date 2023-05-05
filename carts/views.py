from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Cart, CartProduct
from products.models import Product
from .serializers import CartProductSerializer, CartSerializer, CartProductListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class AddToCartView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    def perform_create(self, serializer):
        user = self.request.user    
        serializer.save(user=user)
 
class ListCartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = CartProduct.objects.all()
    serializer_class = CartProductListSerializer

    def get_queryset(self):
        cart = get_object_or_404(Cart.objects.filter(user=self.request.user))
        cart_products = CartProduct.objects.filter(cart=cart)
        return cart_products
        

class CartDetailView(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    lookup_field = 'product_id'

    def get_object(self):
        cart = get_object_or_404(Cart, user=self.request.user)
        get_product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        cart_product = self.queryset.filter(product=get_product, cart=cart).first()

        return cart_product