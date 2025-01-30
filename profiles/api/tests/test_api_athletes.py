from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from profiles.models.athletes import Athlete


class AthleteAPITestCase(TestCase):
    """Test API CRUD for Athlete"""

    def setUp(self):
        """Initialize the test ...."""
        self.client = APIClient()
        self.athlete_data = {
            "first_name": "Luca",
            "last_name": "Bianchi",
            "date_of_birth": "2002-05-20",
            "place_of_birth": "Roma",
            "fiscal_code": "LCBNCH02E20H501K",
            "category": 1
        }
        self.athlete = Athlete.objects.create(**self.athlete_data)
        self.athlete_url = f"/athletes/{self.athlete.id}/"

    # Read Test: GET all athletes
    def test_get_all_athletes(self):
        response = self.client.get("/athletes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # Read Test: GET single athlete
    def test_get_single_athlete(self):
        response = self.client.get(self.athlete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], self.athlete.first_name)

    # Create Test: POST new athlete
    def test_create_athlete(self):
        new_athlete = {
            "first_name": "Marco",
            "last_name": "Rossi",
            "date_of_birth": "2000-10-10",
            "place_of_birth": "Milano",
            "fiscal_code": "MRCRSS00T10F205D",
            "category": 2
        }
        response = self.client.post("/athletes/", new_athlete, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Athlete.objects.count(), 2)  # Ora ci sono 2 atleti

    # Update Test: PUT athlete
    def test_update_athlete(self):
        updated_data = self.athlete_data.copy()
        updated_data["last_name"] = "Verdi"  # Modifica cognome
        response = self.client.put(self.athlete_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.athlete.refresh_from_db()
        self.assertEqual(self.athlete.last_name, "Verdi")

    # Update Test: PATCH athlete
    def test_partial_update_athlete(self):
        response = self.client.patch(self.athlete_url, {"last_name": "Gialli"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.athlete.refresh_from_db()
        self.assertEqual(self.athlete.last_name, "Gialli")

    # Delete Test: DELETE athlete
    def test_delete_athlete(self):
        response = self.client.delete(self.athlete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Athlete.objects.count(), 0)
