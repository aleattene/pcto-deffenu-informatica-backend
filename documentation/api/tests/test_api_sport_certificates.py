from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from documentation.models import SportCertificate
from profiles.models import Athlete, SportDoctor


class SportCertificateAPITestCase(TestCase):
    """Test SportCertificates API CRUD"""

    def setUp(self):
        """Initial Setup ..."""
        self.client = APIClient()

        self.athlete = Athlete.objects.create(
            first_name="Luca",
            last_name="Bianchi",
            date_of_birth="2002-05-20",
            place_of_birth="Roma",
            fiscal_code="LCBNCH02E20H501K",
            category=1
        )

        self.sport_doctor = SportDoctor.objects.create(
            first_name="Mario",
            last_name="Rossi",
            fiscal_code="MRRSS80A01H501Z",
            p_iva="12345678901"
        )

        self.sport_certificate_data = {
            "date_issue": "2024-01-10",
            "date_expiry": "2025-01-10",
            "athlete": self.athlete.id,
            "sport_doctor": self.sport_doctor.id
        }

        self.sport_certificate = SportCertificate.objects.create(**self.sport_certificate_data)
        self.sport_certificate_url = f"/sport_certificates/{self.sport_certificate.id}/"

    # Read Test: GET all sport certificates
    def test_get_all_sport_certificates(self):
        response = self.client.get("/sport_certificates/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # Read Test: GET single sport certificate
    def test_get_single_sport_certificate(self):
        response = self.client.get(self.sport_certificate_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["athlete"], self.athlete.id)

    # Create Test: POST new sport certificate
    def test_create_sport_certificate(self):
        new_certificate = {
            "date_issue": "2024-02-01",
            "date_expiry": "2025-02-01",
            "athlete": self.athlete.id,
            "sport_doctor": self.sport_doctor.id
        }
        response = self.client.post("/sport_certificates/", new_certificate, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SportCertificate.objects.count(), 2)

    # Update Test: PUT sport certificate
    def test_update_sport_certificate(self):
        updated_data = self.sport_certificate_data.copy()
        updated_data["date_expiry"] = "2026-01-10"
        response = self.client.put(self.sport_certificate_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sport_certificate.refresh_from_db()
        self.assertEqual(str(self.sport_certificate.date_expiry), "2026-01-10")

    # Update Test: PATCH sport certificate
    def test_partial_update_sport_certificate(self):
        response = self.client.patch(self.sport_certificate_url, {"date_expiry": "2026-12-01"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sport_certificate.refresh_from_db()
        self.assertEqual(str(self.sport_certificate.date_expiry), "2026-12-01")

    # Delete Test: DELETE sport certificate
    def test_delete_sport_certificate(self):
        response = self.client.delete(self.sport_certificate_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SportCertificate.objects.count(), 0)
