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
# /athletes/ [GET]: list all athletes
# /athletes/ [POST]: create a new athlete
# /athletes/<id>/ [GET]: retrieve an athlete
# /athletes/<id>/ [PUT]: update an athlete
# /athletes/<id>/ [PATCH]: partial update an athlete
# /athletes/<id>/ [DELETE]: delete an athlete

