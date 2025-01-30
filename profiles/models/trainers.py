from django.db import models


class Trainer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nome")
    last_name = models.CharField(max_length=100, verbose_name="Cognome")
    fiscal_code = models.CharField(max_length=16, unique=True, verbose_name="Codice Fiscale")

    class Meta:
        verbose_name = "Allenatore"
        verbose_name_plural = "Allenatori"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.fiscal_code})"

    def __repr__(self):
        return (f"Trainer(first_name={self.first_name}, last_name={self.last_name}, "
                f"fiscal_code={self.fiscal_code})")


# SQL code provided by @DaveAttene
#
# CREATE TABLE Allenatori (
#   id_allenatore INT PRIMARY KEY,
#   nome VARCHAR (255) NOT NULL,
#   cognome VARCHAR (255) NOT NULL,
#   cod_fiscale VARCHAR (16) NOT NULL UNIQUE
# );