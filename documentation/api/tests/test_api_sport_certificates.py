from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from documentation.models.sport_certificates import SportCertificate
from profiles.models.athletes import Athlete, Category
from profiles.models.sport_doctors import SportDoctor


class SportCertificateAPITestCase(TestCase):
    """Test SportCertificates API CRUD"""

    def setUp(self):
        """Initial Setup ..."""
        self.client = APIClient()

        self.category = Category.objects.create(
            code="JM",
            description="Juniores Maschile"
        )

        self.athlete = Athlete.objects.create(
            first_name="Luca",
            last_name="Bianchi",
            date_of_birth="2002-05-20",
            place_of_birth="Roma",
            fiscal_code="LCBNCH02E20H501K",
            category=self.category
        )

        self.sport_doctor = SportDoctor.objects.create(
            first_name="Mario",
            last_name="Rossi",
            vat_number="MRRSS80A01H501Z",
        )

        self.sport_certificate_data = {
            "issue_date": "2024-01-10",
            "expiration_date": "2025-01-10",
            "athlete": self.athlete,
            "sport_doctor": self.sport_doctor
        }

        self.sport_certificate = SportCertificate.objects.create(**self.sport_certificate_data)
        self.sport_certificate_list_url = reverse("documentation:sport-certificates-list")
        self.sport_certificate_detail_url = f"{self.sport_certificate_list_url}{self.sport_certificate.id}/"

    # Read Test: GET all sport certificates
    def test_get_all_sport_certificates(self):
        response = self.client.get(self.sport_certificate_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # Read Test: GET single sport certificate
    def test_get_single_sport_certificate(self):
        response = self.client.get(self.sport_certificate_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["athlete"], self.athlete.id)

    # Create Test: POST new sport certificate
    def test_create_sport_certificate(self):
        new_certificate = {
            "issue_date": "2024-02-01",
            "expiration_date": "2025-02-01",
            "athlete": self.athlete.id,
            "sport_doctor": self.sport_doctor.id
        }
        response = self.client.post(self.sport_certificate_list_url, new_certificate, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SportCertificate.objects.count(), 2)

    # Update Test: PUT sport certificate
    def test_update_sport_certificate(self):
        updated_data = self.sport_certificate_data.copy()
        updated_data["issue_date"] = "2026-01-10"
        updated_data["expiration_date"] = "2026-01-10"
        updated_data["athlete"] = self.athlete.id
        updated_data["sport_doctor"] = self.sport_doctor.id
        response = self.client.put(self.sport_certificate_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sport_certificate.refresh_from_db()
        self.assertEqual(str(self.sport_certificate.issue_date), "2026-01-10")
        self.assertEqual(str(self.sport_certificate.expiration_date), "2026-01-10")
        self.assertEqual(self.sport_certificate.athlete.id, self.athlete.id)
        self.assertEqual(self.sport_certificate.sport_doctor.id, self.sport_doctor.id)

    # Update Test: PATCH sport certificate
    def test_partial_update_sport_certificate(self):
        updated_data = self.sport_certificate_data.copy()
        updated_data["issue_date"] = "2025-12-10"
        updated_data["athlete"] = self.athlete.id
        updated_data["sport_doctor"] = self.sport_doctor.id
        response = self.client.patch(self.sport_certificate_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sport_certificate.refresh_from_db()
        self.assertEqual(str(self.sport_certificate.issue_date), "2025-12-10")
        self.assertEqual(self.sport_certificate.sport_doctor.id, self.sport_doctor.id)

    # Delete Test: DELETE sport certificate
    def test_delete_sport_certificate(self):
        response = self.client.delete(self.sport_certificate_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SportCertificate.objects.count(), 0)
