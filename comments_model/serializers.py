from rest_framework import serializers

from .models import Comment


class CommentSerializerList(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'course_id',
            'text',
        )
