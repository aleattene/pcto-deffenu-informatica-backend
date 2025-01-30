from rest_framework import viewsets
from profiles.models.athletes import Athlete
from profiles.api.serializers.athletes import AthleteSerializer


class AthleteViewSet(viewsets.ModelViewSet):
    """API to handle Athlete CRUD operations"""
    # Retrieve all athletes
    queryset = Athlete.objects.all()
    # Serialize the data to JSON
    serializer_class = AthleteSerializer


# This Viewset automatically generates the following endpoints:
# GET /athletes/ -> list all athletes
# POST /athletes/ -> create a new athlete
# GET /athletes/<id>/ -> retrieve an athlete
# PUT /athletes/<id>/ -> update an athlete
# DELETE /athletes/<id>/ -> delete an athlete
