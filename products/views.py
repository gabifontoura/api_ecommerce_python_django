from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from users.permissions import IsSellerOrAdmin, IsSellerOwnerOrAdmin
from products.models import Product
from products.serializers import ProductSerializer
from drf_spectacular.utils import extend_schema


class CreateProductView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdmin]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(seller_id=self.request.user.id)
    
    @extend_schema(
        operation_id="Create Product",
        responses={200: ProductSerializer},
        description="Create product",
        summary="Create product",
        tags=["Product"]
    )
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_filter = self.request.query_params.get('category')
        name_filter = self.request.query_params.get('name')
        id_filter = self.request.query_params.get('id')

        if id_filter:
            return Product.objects.filter( id = id_filter)

        if category_filter and name_filter:
            return Product.objects.filter( category = category_filter, name = name_filter)

        if category_filter:
            return Product.objects.filter( category = category_filter)

        if name_filter:
            return Product.objects.filter( name = name_filter)

        return Product.objects.all()
    
    @extend_schema(
        operation_id="List Product All | Id | Name | Category",
        responses={200: ProductSerializer},
        description="List Product All | Id | Name | Category",
        summary="List Product",
        tags=["Product"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class ProductDetailView(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOwnerOrAdmin]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_url_kwarg = "product_id"
    
    @extend_schema(
        operation_id="Updated Product",
        responses={200: ProductSerializer},
        description="Updated product by id",
        summary="Updated by id",
        tags=["Product"]
    )
    def patch(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="Updated Product",
        responses={200: ProductSerializer},
        description="Updated Product by id",
        summary="Updated by id",
        tags=["Product"]
    )
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
        
    @extend_schema(
        operation_id="Deleta Product",
        responses={204: ProductSerializer},
        description="Deleta product by id",
        summary="Deleta by id",
        tags=["Product"]
    )
    def delete(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs) 