from rest_framework import serializers

from psb_learning.testing.models import Option, Question, Quizz


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = [
            "id",
            "text"
        ]


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = Question
        fields = [
            "id",
            "text",
            "options"
        ]
