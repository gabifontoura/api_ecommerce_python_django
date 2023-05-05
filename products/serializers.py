from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "value",
            "quantity",
            "is_available",
            "image",
            "seller_id",
        ]
        read_only = ["seller_id", "is_available"]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance: Product, validated_data: dict) -> Product:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if instance.quantity == 0:
            instance.is_available = False
        else:
            instance.is_available = True
            
        instance.save()
        
        return instance
