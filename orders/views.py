from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from orders.serializers import OrderSerializer
from orders.models import Order
from users.permissions import IsIdOwnerOrAdminPermission, IsOrderSellerOrAdmin
from drf_spectacular.utils import extend_schema


class OrderView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @extend_schema(
        operation_id="Create Order",
        responses={200: OrderSerializer},
        description="Create Order",
        summary="Create Order",
        tags=["Order"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class OrderDetailView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOrderSellerOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    lookup_field = "order_id"

    def get_object(self):
        return get_object_or_404(Order, pk=self.kwargs.get("order_id"))

    @extend_schema(
        operation_id="Updated Order",
        responses={200: OrderSerializer},
        description="Updated Order by Id",
        summary="Updated Order by Id",
        tags=["Order"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="Updated Order",
        responses={200: OrderSerializer},
        description="Updated Order by Id",
        summary="Updated Order by Id",
        tags=["Order"],
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class OrderSoldView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsIdOwnerOrAdminPermission]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    lookup_field = "user_id"

    def get_queryset(self):
        return Order.objects.filter(seller_id=self.kwargs.get("user_id"))

    @extend_schema(
        operation_id="List products sold by seller",
        responses={200: OrderSerializer},
        description="list products sold by seller",
        summary="list products sold by seller",
        tags=["Order"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class OrderFinishedView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsIdOwnerOrAdminPermission]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    lookup_field = "user_id"

    def get_queryset(self):
        return Order.objects.filter(user=self.kwargs.get("user_id"))

    @extend_schema(
        operation_id="List my purchased products",
        responses={200: OrderSerializer},
        description="list products purchased by the user",
        summary="list products purchased by the user",
        tags=["Order"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
