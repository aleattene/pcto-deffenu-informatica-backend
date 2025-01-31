from django.test import TestCase
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
        self.trainer_url = f"/trainers/{self.trainer.id}/"

    # Read Test: GET all trainers
    def test_get_all_trainers(self):
        response = self.client.get("/trainers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # Read Test: GET single trainer
    def test_get_single_trainer(self):
        response = self.client.get(self.trainer_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], self.trainer.first_name)

    # Create Test: POST new trainer
    def test_create_trainer(self):
        new_trainer = {
            "first_name": "Marco",
            "last_name": "Verdi",
            "fiscal_code": "MRVRD80A02F205X"
        }
        response = self.client.post("/trainers/", new_trainer, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trainer.objects.count(), 2)

    # Update Test: PUT trainer
    def test_update_trainer(self):
        updated_data = self.trainer_data.copy()
        updated_data["last_name"] = "Bianchi"  # Modifica cognome
        response = self.client.put(self.trainer_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.trainer.refresh_from_db()
        self.assertEqual(self.trainer.last_name, "Bianchi")

    # Partial Update Test: PATCH trainer
    def test_partial_update_trainer(self):
        response = self.client.patch(self.trainer_url, {"last_name": "Neri"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.trainer.refresh_from_db()
        self.assertEqual(self.trainer.last_name, "Neri")

    # Delete Test: DELETE trainer
    def test_delete_trainer(self):
        response = self.client.delete(self.trainer_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Trainer.objects.count(), 0)
