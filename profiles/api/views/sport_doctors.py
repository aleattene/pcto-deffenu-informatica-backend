from rest_framework import viewsets
from profiles.models.sport_doctors import SportDoctor
from profiles.api.serializers.sport_doctors import SportDoctorSerializer


class SportDoctorViewSet(viewsets.ModelViewSet):
    """ViewSet for handle Sport Doctors CRUD API"""
    # Get all Sport Doctors
    queryset = SportDoctor.objects.all()
    # Convert SportDoctors queryset to JSON
    serializer_class = SportDoctorSerializer


# This Viewset automatically generates the following endpoints:
# /sport_doctors/ [GET]: list all Sport Doctors
# /sport_doctors/ [POST]: create a new Sport Doctor
# /sport_doctors/{id}/ [GET]: get a specific Sport Doctor
# /sport_doctors/{id}/ [PUT]: update a specific Sport Doctor
# /sport_doctors/{id}/ [PATCH]: partially update a specific Sport Doctor
# /sport_doctors/{id}/ [DELETE]: delete a specific Sport Doctor
