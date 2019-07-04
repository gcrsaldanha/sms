from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from stock.models import Transaction


class Payer(models.Model):
    name = models.CharField(max_length=255)


class InvoiceCategory(models.Model):
    CATEGORY_INVOICE = ('IN', 'Nota Fiscal')
    CATEGORY_OTHER = ('OT', 'Outro')
    DEFAULT_CATEGORY = CATEGORY_INVOICE
    CATEGORY_CHOICES = (
        CATEGORY_INVOICE,
        CATEGORY_OTHER,
    )

    name = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default=CATEGORY_INVOICE)


class Invoice(models.Model):
    category = models.ForeignKey(InvoiceCategory, on_delete=models.PROTECT)
    payer = models.ForeignKey(Payer, on_delete=models.PROTECT, null=True)
    value = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now)
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT)
    details = models.CharField(max_length=255, blank=True)


class OrderTransaction(models.Model):
    order = models.OneToOneField(Order, on_delete=models.PROTECT)
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)


