from django.db import models
from profiles.models.trainers import Trainer


class Payment(models.Model):
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.PROTECT,
        related_name="payments",
    )

    def __str__(self):
        return f"Payment {self.amount}€ to {self.trainer} on {self.payment_date}"

    def __repr__(self):
        return (f"Payment(id={self.id}, payment_date={self.payment_date}, "
                f"amount={self.amount}, trainer={self.trainer})")


# SQL code provided by @DaveAttene
# CREATE TABLE Compensi (
#   id_compenso INT PRIMARY KEY,
#   data_erogazione DATE NOT NULL,
#   importo DECIMAL (10,2) NOT NULL,
#   id_allenatore INT NOT NULL,
#   FOREIGN KEY (id_allenatore) REFERENCES Allenatori (id_allenatore)
# );