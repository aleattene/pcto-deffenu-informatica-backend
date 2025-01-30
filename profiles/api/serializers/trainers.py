from rest_framework import serializers
from profiles.models.trainers import Trainer


class TrainerSerializer(serializers.ModelSerializer):
    """Serializer for Trainer model"""

    class Meta:
        model = Trainer
        fields = '__all__'
