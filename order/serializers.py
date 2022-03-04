from rest_framework.serializers import ModelSerializer
from .models import Order


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'amount',
            'number_of_people',
            'place_id',
            'place_name',
            'customer_full_name',
            'customer_passport',
            'customer_phone_number',
        )


class OrderViewSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'is_payed',
            'amount',
            'place_id',
            'customer_full_name',
        )