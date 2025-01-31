from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payments.api.views.payments import PaymentViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]

