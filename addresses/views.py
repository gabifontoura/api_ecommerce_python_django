from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsIdOwnerOrAdminPermission
from addresses.models import Address
from .serializers import AddressSerializer
from drf_spectacular.utils import extend_schema

class AddressView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        operation_id="Create Address",
        responses={200: AddressSerializer},
        description="Adds a new address to the logged in user",
        summary="Create a new address",
        tags=["Address"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsIdOwnerOrAdminPermission]

    serializer_class = AddressSerializer
    lookup_field = "user_id"

    def get_queryset(self):
        return Address.objects.filter(user_id=self.kwargs[self.lookup_field])

    @extend_schema(
        operation_id="List Address",
        responses={200: AddressSerializer},
        description="List user addresses by id",
        summary="List by id",
        tags=["Address"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="Updated Address",
        responses={200: AddressSerializer},
        description="Updated user addresses by id",
        summary="Updated by id",
        tags=["Address"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="Updated Address",
        responses={200: AddressSerializer},
        description="Updated Address by id",
        summary="Updated by id",
        tags=["Address"],
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        operation_id="Deleta Address",
        responses={204: AddressSerializer},
        description="Deleta user addresses by id",
        summary="Deleta by id",
        tags=["Address"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
