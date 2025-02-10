from django.contrib import admin
from documentation.models.sport_certificates import SportCertificate
from profiles.models.athletes import Athlete, Category
from profiles.models.trainers import Trainer
from profiles.models.sport_doctors import SportDoctor
from profiles.models.historic_athlete_trainer import HistoricAthleteTrainer


@admin.register(SportCertificate)
class SportCertificateAdmin(admin.ModelAdmin):
    list_display = ("issue_date", "expiration_date", "sport_doctor", "athlete")
    # search_fields = pass

# Register your models here.
