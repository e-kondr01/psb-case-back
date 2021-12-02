from django.urls import path

from .views import QuestionDetailView

urlpatterns = [
    path("/questions/<int:pk>", QuestionDetailView.as_view()),
]
