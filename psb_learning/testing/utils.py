from django.contrib.auth import get_user_model

from .models import Option, Question


def check_answer(question: Question,
                 answer: Option, user: get_user_model()
                 ) -> bool:
    """Проверяет правильность ответа"""
    if answer.question == question and answer.is_correct:
        user.increase_rating()
        return True
    else:
        return False
