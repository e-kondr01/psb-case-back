from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, views
from rest_framework.response import Response

from psb_learning.testing.models import Option, Question
from psb_learning.testing.serializers import AnswerSerializer, QuestionSerializer

from .utils import check_answer


class QuestionDetailView(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class AnswerView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AnswerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        question = get_object_or_404(Question, pk=serializer.validated_data["question"])
        answer = get_object_or_404(Option, pk=serializer.validated_data["option"])

        correct = check_answer(question, answer, self.request.user)
        rating_change = "+5" if correct else "0"
        info = question.correct_info if correct else question.incorrect_info

        next_question = None
        if Question.objects.filter(pk=serializer.validated_data["question"]+1):
            possible_next_question = Question.objects.filter(pk=serializer.validated_data["question"]+1)[0]
            if possible_next_question.quizz == question.quizz:
                next_question = possible_next_question.pk

        resp = {
            "correct": correct,
            "rating_change": rating_change,
            "info": info,
            "next_question": next_question
        }

        return Response(resp)
