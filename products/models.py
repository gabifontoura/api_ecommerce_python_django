from django.db import models


# Create your models here.
class Product(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    is_available = models.BooleanField(default=True)
    image = models.TextField(null=True)

    seller = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="products"
    )
