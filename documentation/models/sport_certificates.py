from django.db import models
from profiles.models.sport_doctors import SportDoctor
from profiles.models.athletes import Athlete


class SportCertificate(models.Model):
    # facility_id = models.CharField(
    #     max_length=50, verbose_name="Identificativo Struttura Erogatrice"
    # )
    issue_date = models.DateField(verbose_name="Data di Emissione")
    expiration_date = models.DateField(verbose_name="Data di Scadenza")

    athlete = models.ForeignKey(
        Athlete,
        on_delete=models.PROTECT,
        verbose_name="Atleta",
        related_name="medical_certificates"
    )

    sport_doctor = models.ForeignKey(
        SportDoctor,
        on_delete=models.PROTECT,
        verbose_name="Medico",
        related_name="certificates"
    )

    class Meta:
        verbose_name = "Certificato Medico Sportivo"
        verbose_name_plural = "Certificati Medico Sportivi"
        # ordering = ["-issued_date"]

    def __str__(self):
        return f"Certificato emesso il {self.issue_date} da {self.sport_doctor} per {self.athlete}"

    def __repr__(self):
        return (f"SportCertificate, issued_date={self.issue_date}, "
                f"expiration_date={self.expiration_date}, doctor={self.sport_doctor}),"
                f"athlete={self.athlete}")



# SQL code provided by @DaveAttene
#  CREATE TABLE CertificazioniSanitarie (
#    id_certificazione INT PRIMARY KEY,
#    data_emissione DATE NOT NULL,
#    data_scadenza DATE NOT NULL,
#    id_atleta INT NOT NULL,
#    id_medico INT NOT NULL,
#    FOREIGN KEY (id_atleta) REFERENCES Atleti (id_atleta),
#    FOREIGN KEY (id_medico) REFERENCES Medici (id_medico)
#  );