from django.contrib import admin

from .models import (
    Catalog,
    Item,
    Manufacturer,
)


admin.site.register(Catalog)
admin.site.register(Item)
admin.site.register(Manufacturer)
