from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from catalog.models import Item, Catalog


class Stock(models.Model):
    name = models.CharField()


class Localization(models.Model):
    name = models.CharField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)


class StockItemAlert(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    alert_minimum_amount = models.PositiveIntegerField()


class Transaction(models.Model):
    DEFAULT_CATEGORY = 1
    CANCEL_CATEGORY = 2
    CATEGORY_CHOICES = (
        (DEFAULT_CATEGORY, 'default transaction'),
        (CANCEL_CATEGORY, 'cancellation transaction'),
    )

    item_catalog = models.ForeignKey(Catalog, on_delete=models.PROTECT)
    stock = models.ForeignKey(Localization, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    originated_from = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=DEFAULT_CATEGORY)
    amount = models.IntegerField()


class Lot(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)
    lot_number = models.CharField()
    expiration_date = models.DateField()
