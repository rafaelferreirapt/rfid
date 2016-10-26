from rest_framework import serializers
from halls.models import Hall, SubHall


class HallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hall
        fields = ('id', 'name', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'name', 'created_at', 'updated_at',)


class SubHallSerializer(serializers.ModelSerializer):
    parent_hall = HallSerializer()

    class Meta:
        model = SubHall
        fields = ('id', 'name', 'parent_hall', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'name', 'parent_hall', 'created_at', 'updated_at',)
