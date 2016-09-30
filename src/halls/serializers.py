from rest_framework import serializers
from .models import Hall, ContentHall


class HallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hall
        fields = ('id', 'tag', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'tag', 'created_at', 'updated_at',)


class ContentHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentHall
        fields = ('url',)
        read_only_fields = ('url',)
