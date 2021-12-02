from rest_framework import serializers

from psb_learning.testing.models import Answer, Question, Quizz


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            "id",
            "text"
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(
        many=True, queryset=Answer.objects.all()
    )

    class Meta:
        fields = [
            "id",
            "text",
            "answers"
        ]
