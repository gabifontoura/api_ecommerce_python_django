from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Cart, CartProduct
from products.models import Product
from .serializers import CartProductSerializer, CartSerializer, CartProductListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema


class AddToCartView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    def perform_create(self, serializer):
        user = self.request.user    
        serializer.save(user=user)
  
    @extend_schema(
        operation_id="Create Cart",
        responses={200: CartProductSerializer},
        description="Create Cart",
        summary="Create Cart",
        tags=["Cart"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
 
class ListCartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = CartProduct.objects.all()
    serializer_class = CartProductListSerializer

    def get_queryset(self):
        cart = get_object_or_404(Cart.objects.filter(user=self.request.user))
        cart_products = CartProduct.objects.filter(cart=cart)
        return cart_products
    
    @extend_schema(
        operation_id="List My Cart",
        responses={200: CartProductSerializer},
        description="List My Cart",
        summary="List My Cart",
        tags=["Cart"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
        

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
    
    @extend_schema(
        operation_id="Updated Cart",
        responses={200: CartProductSerializer},
        description="Updated product inside cart",
        summary="Updated product inside cart",
        tags=["Cart"]
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="Updated Cart",
        responses={200: CartProductSerializer},
        description="Updated product inside cart",
        summary="Updated product inside cart",
        tags=["Cart"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
       
    @extend_schema(
        operation_id="Deleta Cart",
        responses={204: CartProductSerializer},
        description="Deleta product inside cart",
        summary="Deleta product inside cart",
        tags=["Cart"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)