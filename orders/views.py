from django.shortcuts import get_object_or_404, render
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from orders.serializers import OrderSerializer
from orders.models import Order
from users.permissions import IsIdOwnerOrAdminPermission, IsOrderSellerOrAdmin


class OrderView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class OrderDetailView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOrderSellerOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    lookup_field = 'order_id'

    def get_object(self):
        return get_object_or_404(Order, pk = self.kwargs.get('order_id'))
    
class OrderSoldView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsIdOwnerOrAdminPermission]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    lookup_field = 'user_id'

    def get_queryset(self):
        return Order.objects.filter(seller_id = self.kwargs.get('user_id'))
    
class OrderFinishedView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsIdOwnerOrAdminPermission]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    lookup_field = 'user_id'

    def get_queryset(self):
        return Order.objects.filter(user = self.kwargs.get('user_id'))