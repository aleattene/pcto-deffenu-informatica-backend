from django.test import TestCase
from django.urls import reverse
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
            "trainer": self.trainer
        }

        self.payment = Payment.objects.create(**self.payment_data)
        self.payment_list_url = reverse("payments:payments-list")
        self.payment_detail_url = f"{self.payment_list_url}{self.payment.id}/"

    # Read Test: GET all payments
    def test_get_all_payments(self):
        response = self.client.get(self.payment_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # Read Test: GET single payment
    def test_get_single_payment(self):
        response = self.client.get(self.payment_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["payment_date"], "2024-02-01")
        self.assertEqual(response.data["amount"], "1000.00")
        self.assertEqual(response.data["trainer"], self.trainer.id)

    # Create Test: POST new payment
    def test_create_payment(self):
        new_payment = {
            "payment_date": "2024-03-01",
            "amount": "1500.00",
            "trainer": self.trainer.id
        }
        response = self.client.post(self.payment_list_url, new_payment, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 2)

    # Update Test: PUT payment
    def test_update_payment(self):
        updated_data = self.payment_data.copy()
        updated_data["payment_date"] = "2024-04-01"
        updated_data["amount"] = "1200.00"
        updated_data["trainer"] = self.trainer.id
        response = self.client.put(self.payment_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.payment.refresh_from_db()
        self.assertEqual(str(self.payment.payment_date), "2024-04-01")
        self.assertEqual(str(self.payment.amount), "1200.00")
        self.assertEqual(self.payment.trainer.id, self.trainer.id)

    # Update Test: PATCH payment
    def test_partial_update_payment(self):
        updated_data = self.payment_data.copy()
        updated_data["payment_date"] = "2023-01-31"
        updated_data["trainer"] = self.trainer.id
        response = self.client.patch(self.payment_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.payment.refresh_from_db()
        self.assertEqual(str(self.payment.payment_date), "2023-01-31")
        self.assertEqual(self.payment.trainer.id, self.trainer.id)

    # Delete Test: DELETE payment
    def test_delete_payment(self):
        response = self.client.delete(self.payment_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Payment.objects.count(), 0)
