from django.test import TestCase
from django.urls import reverse
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
            "vat_number": "12345678901"
        }
        self.sport_doctor = SportDoctor.objects.create(**self.sport_doctor_data)
        self.sport_doctor_list_url = reverse("profiles:sport-doctors-list")
        self.sport_doctor_detail_url = f"{self.sport_doctor_list_url}{self.sport_doctor.id}/"

    # Get Test : GET all sport doctors
    def test_get_all_sport_doctors(self):
        response = self.client.get(self.sport_doctor_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # Get Test : GET single sport doctor
    def test_get_single_sport_doctor(self):
        response = self.client.get(self.sport_doctor_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], self.sport_doctor.first_name)
        self.assertEqual(response.data["last_name"], self.sport_doctor.last_name)
        self.assertEqual(response.data["vat_number"], self.sport_doctor.vat_number)

    # Create Test : POST new sport doctor
    def test_create_sport_doctor(self):
        new_sport_doctor = {
            "first_name": "Giuseppe",
            "last_name": "Verdi",
            "vat_number": "98765432109"
        }
        response = self.client.post(self.sport_doctor_list_url, new_sport_doctor, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SportDoctor.objects.count(), 2)

    # Update Test : PUT sport doctor
    def test_update_sport_doctor(self):
        updated_data = self.sport_doctor_data.copy()
        updated_data["last_name"] = "Bianchi"
        updated_data["first_name"] = "Gianluca"
        updated_data["vat_number"] = "12345678901"
        response = self.client.put(self.sport_doctor_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sport_doctor.refresh_from_db()
        self.assertEqual(self.sport_doctor.last_name, "Bianchi")
        self.assertEqual(self.sport_doctor.first_name, "Gianluca")
        self.assertEqual(self.sport_doctor.vat_number, "12345678901")

    # Patch Test : PATCH sport doctor
    def test_partial_update_sport_doctor(self):
        updated_data = self.sport_doctor_data.copy()
        updated_data["first_name"] = "Maurizio"
        updated_data["vat_number"] = "10101010101"
        response = self.client.patch(self.sport_doctor_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sport_doctor.refresh_from_db()
        self.assertEqual(self.sport_doctor.first_name, "Maurizio")
        self.assertEqual(self.sport_doctor.vat_number, "10101010101")

    # Delete Test : DELETE sport doctor
    def test_delete_sport_doctor(self):
        response = self.client.delete(self.sport_doctor_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SportDoctor.objects.count(), 0)
