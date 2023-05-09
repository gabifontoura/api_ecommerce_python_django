from django.db import models


class Address(models.Model):
    class Meta:
        ordering = ("id",)

    street = models.CharField(max_length=120)
    number = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="address",
    )
