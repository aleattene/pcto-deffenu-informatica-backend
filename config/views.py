from rest_framework.response import Response
from rest_framework.decorators import api_view


# Placeholder view for the homepage
@api_view(['GET'])
def homepage(request):
    """This is a placeholder view for the homepage"""
    return Response(

        {"message": "API Running Successfully!!!"}
    )
