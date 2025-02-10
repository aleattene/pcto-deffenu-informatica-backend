from rest_framework import viewsets
from profiles.models.athletes import Category
from profiles.api.serializers.athletes_categories import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """API to handle Category CRUD operations"""
    # Retrieve all categories
    queryset = Category.objects.all()
    # Serialize the data to JSON
    serializer_class = CategorySerializer


# This Viewset automatically generates the following endpoints:
# /categories/ [GET]: list all categories
# /categories/ [POST]: create a new category
# /categories/<id>/ [GET]: retrieve a category
# /categories/<id>/ [PUT]: update a category
# /categories/<id>/ [PATCH]: partial update a category
# /categories/<id>/ [DELETE]: delete a category

