from rest_framework import serializers

from .models import Lesson, Question, Work


class LessonSerializerList(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'description',
        )


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