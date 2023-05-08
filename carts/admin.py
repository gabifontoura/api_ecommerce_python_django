from django.contrib import admin

from carts.models import Cart, CartProduct
# Register your models here.
admin.site.register(Cart)
admin.site.register(CartProduct)
