from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User
from products.models import Product
from addresses.models import Address
from orders.models import Order
from django.shortcuts import get_object_or_404

class IsOwnerOrAdminPermission(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, obj: User
    ) -> bool:
        return obj == request.user or request.user.is_superuser

class IsIdOwnerOrAdminPermission(permissions.BasePermission):
    def has_permission(self, request:Request, view:View):
        return (request.user.id == view.kwargs['user_id']) or request.user.is_superuser

class IsSellerOrAdmin(permissions.BasePermission):
    def has_permission(self, request:Request, view:View):
        if request.method == "GET":
            return True
        
        return request.user.role == "Vendedor" or request.user.is_superuser
    
class IsSellerOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request:Request, view:View, obj:Product):
        return (request.user.role == "Vendedor" and request.user.id == obj.seller_id) or request.user.is_superuser
    
class IsOrderSellerOrAdmin(permissions.BasePermission):
    def has_permission(self, request:Request, view:View):
        order = get_object_or_404(Order, id = view.kwargs['order_id'])

        return (request.user.role == "Vendedor" and request.user.id == order.seller_id) or request.user.is_superuser