from rest_framework import serializers

from .models import Like


class LikeSerializerList(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = (
            'profile_id',
        )
