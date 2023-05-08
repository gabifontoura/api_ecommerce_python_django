from rest_framework import serializers
from rest_framework.exceptions import APIException

from addresses.models import Address

class ServiceUnavailable(APIException):
    status_code = 409

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','street','number','city', 'state', 'user_id']
        read_only = ['user_id']

    def create(self, validated_data):
        address = Address.objects.filter(user = validated_data['user']).first()

        if address:
            raise ServiceUnavailable({"detail": "User already has address"})
        
        return super().create(validated_data)
    
