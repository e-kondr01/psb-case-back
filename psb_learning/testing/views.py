from rest_framework import generics

from psb_learning.testing.models import Question
from psb_learning.testing.serializers import QuestionSerializer


class QuestionDetailView(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
