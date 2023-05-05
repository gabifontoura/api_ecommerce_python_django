from rest_framework import serializers

from addresses.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','street','number','city', 'state', 'user_id']
        read_only = ['user_id']