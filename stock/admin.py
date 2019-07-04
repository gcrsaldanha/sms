from django.contrib import admin

from .models import (
    Localization,
    Lot,
    Stock,
    StockItemAlert,
    Transaction,
)


admin.site.register(Localization)
admin.site.register(Lot)
admin.site.register(Stock)
admin.site.register(StockItemAlert)
admin.site.register(Transaction)
