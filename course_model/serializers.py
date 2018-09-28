from rest_framework import serializers

from test_student_model.serializers import WorkSerializerList, LessonSerializerList
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
    work = serializers.SerializerMethodField()
    lesson = serializers.SerializerMethodField()

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
            'work',
            'lesson'
        )

    def get_work(self, obj):
        works = WorkSerializerList(obj.work.all(), many=True)
        return works.data

    def get_lesson(self, obj):
        lessons = LessonSerializerList(obj.work.all(), many=True)
        return lessons.data