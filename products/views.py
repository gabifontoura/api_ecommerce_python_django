from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(seller_id=self.request.user.id)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
