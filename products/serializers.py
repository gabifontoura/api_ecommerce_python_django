from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "value",
            "quantity",
            "is_available",
            "image",
            "seller_id",
        ]

        extra_kwargs = {"seller_id": {"write_only": True}}

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance: Product, validated_data: dict) -> Product:
        for key, value in validated_data.items():
            setattr(instance, key, value)
