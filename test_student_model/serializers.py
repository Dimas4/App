from rest_framework import serializers

from homework_model.serializers import HomeWorkSerializerList
from homework_model.models import HomeWork
from .models import Lesson, Question, Work


class LessonSerializerList(serializers.HyperlinkedModelSerializer):
    home_work = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = (
            'description',
            'home_work'
        )

    def get_home_work(self, obj):
        home_works = HomeWorkSerializerList(HomeWork.objects.filter(lesson_id=obj.id), many=True)
        return home_works.data


class QuestionSerializerList(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = (
            'text',
            'answer',
        )


class WorkSerializerList(serializers.HyperlinkedModelSerializer):
    question = serializers.SerializerMethodField()

    class Meta:
        model = Work
        fields = (
            'description',
            'type',
            'question',
        )

    def get_question(self, obj):
        questions = QuestionSerializerList(obj.question.all(), many=True)
        return questions.data