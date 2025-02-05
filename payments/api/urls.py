from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payments.api.views.payments import PaymentViewSet

# Application namespace
app_name = 'payments'

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [
    # Endpoint: api/v1/payments/payments/ (GET, POST, PUT, DELETE)
    path('', include(router.urls)),
]
