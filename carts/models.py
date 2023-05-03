from django.db import models


class Cart(models.Model): 
    class Meta:
        ordering = ["id"]

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name='cart'
    )
    
    cart_products = models.ManyToManyField(
        "products.Product",
        through="carts.CartProduct",
        related_name="cart_products",
    )

class CartProduct(models.Model):
    class Meta:
        ordering = ["id"]

    product_quantity = models.PositiveIntegerField(default=1)

    cart = models.ForeignKey(
        "carts.Cart",
        on_delete=models.CASCADE,
        related_name='pivo_cart'
    )

    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='pivo_product'
    )

