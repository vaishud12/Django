from rest_framework import serializers
from products.models import Product

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'tags')  # Corrected 'quanntity' to 'quantity'

class ReadProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'created_at', 'price', 'quantity', 'tags')  # Corrected 'field' to 'fields'