from rest_framework import serializers

from .models import HomeWork


class HomeWorkSerializerList(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeWork
        fields = (
            'text',
        )
