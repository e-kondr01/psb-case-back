from django.urls import path

from .views import AnswerView, QuestionDetailView

urlpatterns = [
    path("/questions/<int:pk>", QuestionDetailView.as_view()),
    path("/answer", AnswerView.as_view())
]
