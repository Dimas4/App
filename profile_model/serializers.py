from rest_framework import serializers

from .models import Profile


class ProfileSerializerList(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='one_profile',
        lookup_field='id'
    )

    class Meta:
        model = Profile
        fields = (
            'url',
            'first_name',
            'second_name',
        )


class ProfileSerializerOne(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'second_name',
            'about_me',
            'email',
        )
