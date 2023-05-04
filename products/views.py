from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from users.permissions import IsSellerOrAdmin, IsSellerOwnerOrAdmin
from products.models import Product
from products.serializers import ProductSerializer


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CreateProductView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdmin]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(seller_id=self.request.user.id)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOwnerOrAdmin]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_url_kwarg = "product_id"
