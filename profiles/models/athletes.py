from django.db import models


class Athlete(models.Model):
    """Model representing an athlete."""
    first_name = models.CharField(max_length=100, verbose_name="Nome")
    last_name = models.CharField(max_length=100, verbose_name="Cognome")
    date_of_birth = models.DateField(verbose_name="Data di Nascita")
    place_of_birth = models.CharField(max_length=150, verbose_name="Luogo di Nascita")
    fiscal_code = models.CharField(max_length=16, unique=True, verbose_name="Codice Fiscale")
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        verbose_name="Categoria",
        related_name="athletes"
    )

    trainer = models.ForeignKey(
        "Trainer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Trainer",
        related_name="athletes"
    )

    class Meta:
        verbose_name = "Atleta"
        verbose_name_plural = "Atleti"
        # ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.fiscal_code})"

    def __repr__(self):
        return (f"Athlete(first_name={self.first_name}, last_name={self.last_name}, "
                f"date_of_birth={self.date_of_birth}, fiscal_code={self.fiscal_code})")


class Category(models.Model):
    code = models.CharField(max_length=4, unique=True)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"
        # ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.description}"

    def __repr__(self):
        return f"Category(code={self.code}, description={self.description}, age_range={self.age_range})"


# SQL code provided by @DaveAttene
#
# CREATE TABLE Atleti (
#     id_atleta INT PRIMARY KEY,
#     nome VARCHAR (255) NOT NULL,
#     cognome VARCHAR (255) NOT NULL,
#     data_nascita DATE NOT NULL,
#     luogo_nascita VARCHAR (255) NOT NULL,
#     cod_fiscale VARCHAR (16) NOT NULL UNIQUE,
#     id_categoria INT NOT NULL,
#     FOREIGN KEY (id_categoria) REFERENCES Categorie (id_categoria)
# );
#
#  CREATE TABLE Categorie (
#    id_categoria INT PRIMARY KEY,
#    codice INT NOT NULL,
#    descrizione VARCHAR (255) NOT NULL
#  );
