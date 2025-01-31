from rest_framework import viewsets
from payments.models.payments import Payment
from payments.api.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """ViewSet for handle Payment API CRUD"""
    # Get all payments
    queryset = Payment.objects.all()
    # Convert Payment queryset to JSON
    serializer_class = PaymentSerializer


# This Viewset automatically generates the following endpoints:
# /payments/ [GET]: list all payments
# /payments/ [POST]: create a new payment
# /payments/{id}/ [GET]: retrieve a payment
# /payments/{id}/ [PUT]: update a payment
# /payments/{id}/ [PATCH]: partial update a payment
# /payments/{id}/ [DELETE]: delete a payment
