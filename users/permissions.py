from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User
from products.models import Product
from addresses.models import Address

class IsOwnerOrAdminPermission(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, obj: User
    ) -> bool:
        return obj == request.user or request.user.is_superuser
    

class IsAddressOwnerOrAdminPermission(permissions.BasePermission):

    def has_permission(self, request:Request, view:View):
        # import ipdb
        # ipdb.set_trace()
        # address_data = Address.objects.get(user_id = request.user.id)

        return (request.user.id == view.kwargs['user_id']) or request.user.is_superuser


class IsSellerOrAdmin(permissions.BasePermission):
    def has_permission(self, request:Request, view:View):
        return request.user.role == "Vendedor" or request.user.is_superuser
    
class IsSellerOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request:Request, view:View, obj):
        product_data = Product.objects.get(id = request.query_params['product_id'])

        return (request.user.role == "Vendedor" and request.user.id == product_data.seller_id) or request.user.is_superuser
    