from rest_framework import serializers

from .models import Item, Catalog, Manufacturer


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'
