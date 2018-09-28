from rest_framework import serializers

from test_student_model.serializers import LessonSerializerWithOutHomeWork
from homework_model.serializers import HomeWorkSerializerList
from comments_model.serializers import CommentSerializerList
from contact_model.serializers import ContactSerializerList
from message_model.serializers import MessageSerializerList
from course_model.serializers import CourseSerializerOne
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
    contact = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    my_homework = serializers.SerializerMethodField()
    saved_lesson = serializers.SerializerMethodField()
    message = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'second_name',
            'avatar',
            'about_me',
            'email',
            'contact',
            'course',
            'my_homework',
            'saved_lesson',
            'message',
            'comment',
        )

    def get_contact(self, obj):
        contacts = ContactSerializerList(obj.contact.all(), many=True)
        return contacts.data

    def get_course(self, obj):
        courses = CourseSerializerOne(obj.course.all(), many=True)
        return courses.data

    def get_my_homework(self, obj):
        my_homeworks = HomeWorkSerializerList(obj.my_homework.all(), many=True)
        return my_homeworks.data

    def get_saved_lesson(self, obj):
        saved_lessons = LessonSerializerWithOutHomeWork(obj.saved_lesson.all(), many=True)
        return saved_lessons.data

    def get_message(self, obj):
        messages = MessageSerializerList(obj.message.all(), many=True)
        return messages.data

    def get_comment(self, obj):
        comments = CommentSerializerList(obj.comment.all(), many=True)
        return comments.data
