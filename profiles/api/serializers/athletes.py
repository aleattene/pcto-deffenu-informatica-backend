from rest_framework import serializers
from profiles.models.athletes import Athlete


class AthleteSerializer(serializers.ModelSerializer):
    """Serializer for the Athlete model"""

    class Meta:
        model = Athlete
        # fields = "__all__"
        exclude = ("trainers",)

