from rest_framework import serializers
from profiles.models.athletes import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the Athlete's Category model"""

    class Meta:
        model = Category
        fields = '__all__'

