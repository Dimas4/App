from rest_framework import serializers

from .models import Course


class CourseSerializerList(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='one_course',
        lookup_field='id'
    )

    class Meta:
        model = Course
        fields = (
            'url',
            'name',
            'description',
            'banner',
        )


class CourseSerializerOne(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = (
            'training',
            'name',
            'description',
            'banner',
            'upcoming_webinar',
            'progress',
            'leave_course',
            'price',
            'student_count',
            'price',
        )
