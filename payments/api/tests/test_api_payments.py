from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from payments.models.payments import Payment
from profiles.models.trainers import Trainer


class PaymentAPITestCase(TestCase):
    """Test Payment API CRUD"""

    def setUp(self):
        """Initial Setup ... """
        self.client = APIClient()

        self.trainer = Trainer.objects.create(
            first_name="Marco",
            last_name="Bianchi",
            fiscal_code="MRCBNC80A01H501Z"
        )

        self.payment_data = {
            "payment_date": "2024-02-01",
            "amount": "1000.00",
            "trainer": self.trainer.id
        }

        self.payment = Payment.objects.create(**self.payment_data)
        self.payment_url = f"/payments/{self.payment.id}/"

    # Read Test: GET all payments
    def test_get_all_payments(self):
        response = self.client.get("/payments/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # Read Test: GET single payment
    def test_get_single_payment(self):
        response = self.client.get(self.payment_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["amount"], "1000.00")

    # Create Test: POST new payment
    def test_create_payment(self):
        new_payment = {
            "payment_date": "2024-03-01",
            "amount": "1500.00",
            "trainer": self.trainer.id
        }
        response = self.client.post("/payments/", new_payment, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 2)

    # Update Test: PUT payment
    def test_update_payment(self):
        updated_data = self.payment_data.copy()
        updated_data["amount"] = "1200.00"
        response = self.client.put(self.payment_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.payment.refresh_from_db()
        self.assertEqual(str(self.payment.amount), "1200.00")

    # Update Test: PATCH payment
    def test_partial_update_payment(self):
        response = self.client.patch(self.payment_url, {"amount": "1800.00"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.payment.refresh_from_db()
        self.assertEqual(str(self.payment.amount), "1800.00")

    # Delete Test: DELETE payment
    def test_delete_payment(self):
        response = self.client.delete(self.payment_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Payment.objects.count(), 0)
