"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles.api.views.sport_doctors import SportDoctorViewSet
from profiles.views.athletes import AthleteViewSet
from profiles.api.views.trainers import TrainerViewSet
# Create a router and register our viewset with it.
router = DefaultRouter(

router.register(r'sport_doctors', SportDoctorViewSet, basename='sportdoctor')
router.register(r'trainers', TrainerViewSet, basename='trainers')
router.register(r'athletes', AthleteViewSet, basename='athlete')


urlpatterns = [
    # Athletes
    path("", include(router.urls)),
    # Trainers
    path('trainers/'),
    # Sport Doctors
    path('sport_doctors/'),
]