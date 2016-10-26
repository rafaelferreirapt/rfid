from rest_framework import serializers
from halls.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'name', 'description', 'created_at', 'updated_at',)
