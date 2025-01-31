from rest_framework import viewsets
from profiles.models.trainers import Trainer
from profiles.api.serializers.trainers import TrainerSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    """ViewSet for handle the TRAINER endpoints (CRUD)"""
    # Get all the trainers
    queryset = Trainer.objects.all()
    # Use the TrainerSerializer to serialize the data (from data to JSON)
    serializer_class = TrainerSerializer

# This viewset automatically generates the following endpoints:
# /trainers/ [GET]: list all trainers
# /trainers/ [POST]: create a new trainer
# /trainers/{id}/ [GET]: retrieve a trainer
# /trainers/{id}/ [PUT]: update a trainer
# /trainers/{id}/ [PATCH]: partial update a trainer
# /trainers/{id}/ [DELETE]: delete a trainer
