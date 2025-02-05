from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles.api.views.athletes import AthleteViewSet
from profiles.api.views.trainers import TrainerViewSet
from profiles.api.views.sport_doctors import SportDoctorViewSet

# Application namespace
app_name = 'profiles'

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'athletes', AthleteViewSet, basename='athletes')
router.register(r'trainers', TrainerViewSet, basename='trainers')
router.register(r'sport-doctors', SportDoctorViewSet, basename='sport-doctors')

urlpatterns = [
    # Athletes, Trainers and Sport Doctors
    path("", include(router.urls)),
]