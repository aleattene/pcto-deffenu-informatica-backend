from rest_framework import serializers
from documentation.models.sport_certificates import SportCertificate


class SportCertificateSerializer(serializers.ModelSerializer):
    """Serializer for SportCertificate model"""

    class Meta:
        model = SportCertificate
        fields = '__all__'



