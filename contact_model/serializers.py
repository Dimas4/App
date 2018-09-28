from rest_framework import serializers

from .models import Contact


class ContactSerializerList(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contact
        fields = (
            'name',
            'contact',
        )
