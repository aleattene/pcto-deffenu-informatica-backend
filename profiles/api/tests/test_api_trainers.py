from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from profiles.models.trainers import Trainer


class TrainerAPITestCase(TestCase):
    """Test Trainers API CRUD"""

    def setUp(self):
        """Initial Setup .... """
        self.client = APIClient()
        self.trainer_data = {
            "first_name": "Giovanni",
            "last_name": "Rossi",
            "fiscal_code": "GVRRSS80A01H501Z"
        }
        self.trainer = Trainer.objects.create(**self.trainer_data)
        self.trainer_list_url = reverse("profiles:trainers-list")
        self.trainer_detail_url = f"{self.trainer_list_url}{self.trainer.id}/"

    # Read Test: GET all trainers
    def test_get_all_trainers(self):
        response = self.client.get(self.trainer_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # Read Test: GET single trainer
    def test_get_single_trainer(self):
        response = self.client.get(self.trainer_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], self.trainer.first_name)
        self.assertEqual(response.data["last_name"], self.trainer.last_name)
        self.assertEqual(response.data["fiscal_code"], self.trainer.fiscal_code)

    # Create Test: POST new trainer
    def test_create_trainer(self):
        new_trainer = {
            "first_name": "Marco",
            "last_name": "Verdi",
            "fiscal_code": "MRVRD80A02F205X"
        }
        response = self.client.post(self.trainer_list_url, new_trainer, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trainer.objects.count(), 2)

    # Update Test: PUT trainer
    def test_update_trainer(self):
        updated_data = self.trainer_data.copy()
        updated_data["last_name"] = "Bianchi"
        updated_data["first_name"] = "Gianluca"
        updated_data["fiscal_code"] = "GVRRSS80A01H501Z"
        response = self.client.put(self.trainer_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.trainer.refresh_from_db()
        self.assertEqual(self.trainer.last_name, "Bianchi")
        self.assertEqual(self.trainer.first_name, "Gianluca")
        self.assertEqual(self.trainer.fiscal_code, "GVRRSS80A01H501Z")

    # Partial Update Test: PATCH trainer
    def test_partial_update_trainer(self):
        updated_data = self.trainer_data.copy()
        updated_data["last_name"] = "Neri"
        updated_data["fiscal_code"] = "GVRRSS80A01H501Z"
        response = self.client.patch(self.trainer_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.trainer.refresh_from_db()
        self.assertEqual(self.trainer.last_name, "Neri")
        self.assertEqual(self.trainer.fiscal_code, "GVRRSS80A01H501Z")

    # Delete Test: DELETE trainer
    def test_delete_trainer(self):
        response = self.client.delete(self.trainer_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Trainer.objects.count(), 0)
