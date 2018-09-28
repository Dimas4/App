from rest_framework import serializers

from .models import Direction


class DirectionSerializerList(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direction
        fields = (
            'name',
            'direction',
        )
