from django.contrib import admin

from .models import (
    Invoice,
    InvoiceCategory,
    Order,
    OrderTransaction,
    Payer,
)


admin.site.register(Invoice)
admin.site.register(InvoiceCategory)
admin.site.register(Order)
admin.site.register(OrderTransaction)
admin.site.register(Payer)
