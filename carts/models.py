from django.db import models


class Cart(models.Model): 
    class Meta:
        ordering = ["id"]

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name='cart'
    )

    products = models.JSONField()

class CartProduct(models.Model):
    class Meta:
        ordering = ["id"]

    product_quantity = models.PositiveIntegerField(default=1)

    cart = models.ForeignKey(
        "carts.Cart",
        on_delete=models.CASCADE,
        related_name='cart_products'
    )

    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='cart_products'
    )

