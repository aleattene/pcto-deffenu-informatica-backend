from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from profiles.models.athletes import Athlete, Category


class AthleteAPITestCase(TestCase):
    """Test API CRUD for Athlete"""

    def setUp(self):
        """Initialize the test ...."""
        self.client = APIClient()
        self.category = Category.objects.create(code="AM", description="Allievo Maschile")
        self.athlete_data = {
            "first_name": "Luca",
            "last_name": "Bianchi",
            "date_of_birth": "2002-05-20",
            "place_of_birth": "Roma",
            "fiscal_code": "LCBNCH02E20H501K",
            "category": self.category
        }
        self.athlete = Athlete.objects.create(**self.athlete_data)
        self.athlete_list_url = reverse("profiles:athletes-list")
        self.athlete_detail_url = f"{self.athlete_list_url}{self.athlete.id}/"

    # Read Test: GET all athletes
    def test_get_all_athletes(self):
        response = self.client.get(self.athlete_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # Read Test: GET single athlete
    def test_get_single_athlete(self):
        response = self.client.get(self.athlete_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], self.athlete.first_name)
        self.assertEqual(response.data["last_name"], self.athlete.last_name)
        self.assertEqual(response.data["date_of_birth"], str(self.athlete.date_of_birth))
        self.assertEqual(response.data["place_of_birth"], self.athlete.place_of_birth)
        self.assertEqual(response.data["fiscal_code"], self.athlete.fiscal_code)
        self.assertEqual(response.data["category"], self.athlete.category.id)

    # Create Test: POST new athlete
    def test_create_athlete(self):
        self.category = Category.objects.create(code="AF", description="Allieva Femminile")
        new_athlete = {
            "first_name": "Marco",
            "last_name": "Rossi",
            "date_of_birth": "2000-10-10",
            "place_of_birth": "Milano",
            "fiscal_code": "MRCRSS00T10F205D",
            "category": self.category.id
        }
        response = self.client.post(self.athlete_list_url, new_athlete, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Athlete.objects.count(), 2)

    # Update Test: PUT athlete
    def test_update_athlete(self):
        updated_data = self.athlete_data.copy()
        updated_data["last_name"] = "Verdi"
        updated_data["category"] = self.category.id
        response = self.client.put(self.athlete_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.athlete.refresh_from_db()
        self.assertEqual(self.athlete.last_name, "Verdi")

    # Update Test: PATCH athlete
    def test_partial_update_athlete(self):
        updated_data = self.athlete_data.copy()
        updated_data["last_name"] = "Gialli"
        updated_data["first_name"] = "Gianluca"
        updated_data["fiscal_code"] = "LCBNCH02E20H501K"
        updated_data["category"] = self.category.id
        response = self.client.patch(self.athlete_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.athlete.refresh_from_db()
        self.assertEqual(self.athlete.last_name, "Gialli")
        self.assertEqual(self.athlete.first_name, "Gianluca")
        self.assertEqual(self.athlete.fiscal_code, "LCBNCH02E20H501K")
        self.assertEqual(self.athlete.category.id, self.category.id)

    # Delete Test: DELETE athlete
    def test_delete_athlete(self):
        response = self.client.delete(self.athlete_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Athlete.objects.count(), 0)
