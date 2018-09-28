from rest_framework import serializers

from test_student_model.serializers import WorkSerializerList, LessonSerializerList
from direction_course_model.serializers import DirectionSerializerList
from direction_course_model.models import Direction
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
    direction = serializers.SerializerMethodField('direction_data')

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
            'lesson',
            'direction'
        )

    def get_work(self, obj):
        works = WorkSerializerList(obj.work.all(), many=True)
        return works.data

    def get_lesson(self, obj):
        lessons = LessonSerializerList(obj.work.all(), many=True)
        return lessons.data

    def direction_data(self, obj):
        direction = DirectionSerializerList(Direction.objects.filter(course_id=obj.id), many=True)
        return direction.data
