from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Cart, CartProduct
from .serializers import CartSerializer, CartProductSerializer


class AddToCartView(generics.CreateAPIView):
    serializer_class = CartProductSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
 


class RemoveFromCartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
