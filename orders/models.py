from django.db import models

class RatingChoices(models.TextChoices):
        PR = "Pedido Realizado"
        PeA = "Pedido Em Andamento"
        E = "Entregue"
    
class Order(models.Model):
    class Meta:
        ordering = ["id"]

    status = models.CharField(choices=RatingChoices.choices, default=RatingChoices.PR)
    
    created_at = models.DateTimeField(auto_now_add=True)

    seller_id = models.IntegerField(null=True, default=None)

    products = models.JSONField()

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name='orders'
    )
