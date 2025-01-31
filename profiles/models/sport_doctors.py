from django.db import models


class SportDoctor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nome")
    last_name = models.CharField(max_length=100, verbose_name="Cognome")
    vat_number = models.CharField(max_length=11, unique=True, verbose_name="Partita IVA")

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medici"
        # ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - P.IVA: {self.vat_number}"

    def __repr__(self):
        return (f"SportDoctor(first_name={self.first_name}, last_name={self.last_name}, "
                f"vat_number={self.vat_number})")


# SQL code provided by @DaveAttene
#
# CREATE TABLE Medici(
#   id_medico INT PRIMARY KEY,
#   p_iva VARCHAR(11) NOT NULL,
#   nome VARCHAR(255) NOT NULL,
#   cognome VARCHAR(255) NOT NULL
# );
