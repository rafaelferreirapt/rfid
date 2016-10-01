from rest_framework import serializers
from halls.models import Hall


class HallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hall
        fields = ('id', 'tag', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'tag', 'created_at', 'updated_at',)
