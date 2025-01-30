from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from profiles.models.sport_doctors import SportDoctor


class SportDoctorAPITestCase(TestCase):
    """Test SportDoctor API CRUD"""

    def setUp(self):
        """Initialize test data ...."""
        self.client = APIClient()
        self.sport_doctor_data = {
            "first_name": "Mario",
            "last_name": "Rossi",
            "fiscal_code": "MRRSS80A01H501Z",
            "p_iva": "12345678901"
        }
        self.sport_doctor = SportDoctor.objects.create(**self.sport_doctor_data)
        self.sport_doctor_url = f"/sport_doctors/{self.sport_doctor.id}/"

    # Get Test : GET all sport doctors
    def test_get_all_sport_doctors(self):
        response = self.client.get("/sport_doctors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # Get Test : GET single sport doctor
    def test_get_single_sport_doctor(self):
        response = self.client.get(self.sport_doctor_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], self.sport_doctor.first_name)

    # Create Test : POST new sport doctor
    def test_create_sport_doctor(self):
        new_sport_doctor = {
            "first_name": "Giuseppe",
            "last_name": "Verdi",
            "fiscal_code": "GSPVRD80A02F205X",
            "p_iva": "98765432109"
        }
        response = self.client.post("/sport_doctors/", new_sport_doctor, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SportDoctor.objects.count(), 2)

    # Update Test : PUT sport doctor
    def test_update_sport_doctor(self):
        updated_data = self.sport_doctor_data.copy()
        updated_data["last_name"] = "Bianchi"
        response = self.client.put(self.sport_doctor_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sport_doctor.refresh_from_db()
        self.assertEqual(self.sport_doctor.last_name, "Bianchi")

    # Patch Test : PATCH sport doctor
    def test_partial_update_sport_doctor(self):
        response = self.client.patch(self.sport_doctor_url, {"last_name": "Gialli"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sport_doctor.refresh_from_db()
        self.assertEqual(self.sport_doctor.last_name, "Gialli")

    # Delete Test : DELETE sport doctor
    def test_delete_sport_doctor(self):
        response = self.client.delete(self.sport_doctor_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SportDoctor.objects.count(), 0)
