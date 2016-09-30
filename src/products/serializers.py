from rest_framework import serializers
from .models import ProductHalls, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'brand', 'price', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'name', 'description', 'brand', 'price', 'created_at', 'updated_at',)


class ProductHallsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductHalls
        fields = ('product', 'hall',)
        read_only_fields = ('product', 'hall',)
