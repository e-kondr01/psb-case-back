from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, views
from rest_framework.response import Response

from psb_learning.testing.models import Option, Question
from psb_learning.testing.serializers import AnswerSerializer, QuestionSerializer


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

        if answer.question == question and answer.is_correct:
            correct = True
            self.request.user.rating += 5
            self.request.user.save()

        else:
            correct = False

        next_question = None
        if Option.objects.filter(pk=serializer.validated_data["option"]+1):
            possible_next_option = Option.objects.filter(pk=serializer.validated_data["option"]+1)[0]
            if possible_next_option.question == question:
                next_question = possible_next_option.pk

        resp = {
            "correct": correct,
            "next_question": next_question
        }

        return Response(resp)
