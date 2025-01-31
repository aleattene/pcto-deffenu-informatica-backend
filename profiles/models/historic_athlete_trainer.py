from django.db import models


class HistoricAthleteTrainer(models.Model):
    athlete = models.ForeignKey(
        "Athlete",
        on_delete=models.PROTECT,
        related_name="historic_trainer_links"
    )
    trainer = models.ForeignKey(
        "Trainer",
        on_delete=models.PROTECT,
        related_name="historic_athlete_links"
    )

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Storico Atleta Allenatore"
        verbose_name_plural = "Storico Atleti Allenatori"

    def __str__(self):
        return f"{self.athlete} - {self.trainer} (from {self.start_date} to {self.end_date})"

    def __repr__(self):
        return (f"HistoricTrainerAthlete(athlete={self.athlete}, trainer={self.trainer}, "
                f"start_date={self.start_date}, end_date={self.end_date})")


# SQL code provided by @DaveAttene
#
# CREATE TABLE StoricoAtletiAllenatori (
#   id_storico INT PRIMARY KEY,
#   id_allenatore INT NOT NULL,
#   id_atleta INT NOT NULL,
#   data_inizio DATE NOT NULL,
#   data_fine DATE NOT NULL,
#   FOREIGN KEY (id_allenatore) REFERENCES Allenatori (id_allenatori),
#   FOREIGN KEY (id_atleta) REFERENCES Atleti (id_atleta)
#  );
