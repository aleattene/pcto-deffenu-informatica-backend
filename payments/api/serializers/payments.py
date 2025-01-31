from rest_framework import serializers
from payments.models.payments import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Serializer for Payment model"""

    class Meta:
        model = Payment
        fields = '__all__'

