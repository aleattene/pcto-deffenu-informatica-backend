from rest_framework import serializers
from profiles.models.sport_doctors import SportDoctor


class SportDoctorSerializer(serializers.ModelSerializer):
    """Serializer for SportDoctor model"""

    class Meta:
        model = SportDoctor
        fields = '__all__'
