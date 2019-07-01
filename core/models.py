from django.db import models


class Amount(models.Model):
    UNIT_UNITARY = ('un', 'un')
    UNIT_LITER = ('L', 'L')
    UNIT_KILOGRAM = ('Kg', 'Kg')
    UNIT_CHOICES = (
        UNIT_UNITARY,
        UNIT_LITER,
        UNIT_KILOGRAM
    )

    unit = models.CharField(choices=UNIT_CHOICES, default=UNIT_UNITARY)
    value = models.DecimalField(max_digits=7, decimal_places=3, default=1)


