from django.db import models


class Manufacturer(models.Model):
    name = models.CharField()


class Item(models.Model):
    name = models.CharField()


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
    catalog_number = models.CharField(blank=True)
    stock_units = models.PositiveIntegerField()
