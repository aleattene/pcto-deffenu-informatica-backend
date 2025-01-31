from rest_framework import viewsets
from documentation.models.sport_certificates import SportCertificate
from documentation.api.serializers.sport_certificates import SportCertificateSerializer


class SportCertificateViewSet(viewsets.ModelViewSet):
    """ViewSet for handle SportCertificate CRUD API"""
    # Get all SportCertificates
    queryset = SportCertificate.objects.all()
    # Convert SportCertificate queryset to JSON
    serializer_class = SportCertificateSerializer


# This Viewset automatically generates the following endpoints:
# /sport_certificates/ [GET]: list all SportCertificates
# /sport_certificates/ [POST]: create a new SportCertificate
# /sport_certificates/{id}/ [GET]: retrieve a SportCertificate
# /sport_certificates/{id}/ [PUT]: update a SportCertificate
# /sport_certificates/{id}/ [PATCH]: partial update a SportCertificate
# /sport_certificates/{id}/ [DELETE]: delete a SportCertificate
