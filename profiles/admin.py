from django.contrib import admin
from profiles.models.athletes import Athlete, Category
from profiles.models.trainers import Trainer
from profiles.models.sport_doctors import SportDoctor
from profiles.models.historic_athlete_trainer import HistoricAthleteTrainer


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "fiscal_code", "category")
    search_fields = ("first_name", "last_name", "fiscal_code")


@admin.register(Category)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ("code", "description")
    search_fields = ("code", "description")


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "fiscal_code")
    search_fields = ("first_name", "last_name", "fiscal_code")


@admin.register(SportDoctor)
class SportDoctorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "vat_number")
    search_fields = ("first_name", "last_name", "vat_number")


@admin.register(HistoricAthleteTrainer)
class HistoricTrainerAthleteAdmin(admin.ModelAdmin):
    list_display = ("trainer", "athlete", "start_date", "end_date")
    search_fields = ("trainer__first_name", "trainer__last_name", "athlete__first_name", "athlete__last_name")
    list_filter = ("start_date", "end_date")
