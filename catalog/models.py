from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)


class Item(models.Model):
    name = models.CharField(max_length=255)


class Catalog(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['manufacturer', 'catalog_number'],
                name='unique catalog',
            ),
        ]

    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.PROTECT)
    catalog_number = models.CharField(max_length=255, blank=True)
    stock_units = models.PositiveIntegerField()
