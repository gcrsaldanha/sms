from rest_framework import generics

from .models import (
    Item,
    Manufacturer,
    Catalog,
)
from .serializers import (
    ItemSerializer,
    ManufacturerSerializer,
    CatalogSerializer,
)


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ManufacturerListCreate(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CatalogListCreate(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
