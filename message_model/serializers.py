from rest_framework import serializers

from .models import Message


class MessageSerializerList(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = (
            'profile_id',
            'text',
            'document',
        )
